import sys
from time import sleep
sys.path.append('../lib')
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cfclient.utils.logconfigreader import LogConfig
from threading import Thread



import logging
logging.basicConfig(level=logging.ERROR)

class Crazy:
    def __init__(self,x,y,z,conn_status):

        # zmienne pomocnicze w obsludze GUI
        self.conn=conn_status
        self.x=x
        self.y=y
        self.z=z
        self.thrust=0
        self.startup=True
        self.is_connected=False

        # ustawienia biblioteki cf
        self.cf=Crazyflie()
        self.cf.connected.add_callback(self.connected)
        self.cf.disconnected.add_callback(self.disconnected)

    #funkcja inicjujaca polaczenie
    def connect(self,uri):
        self.cf.open_link(uri)
        self.is_connected=True

    # funkcja wywolywana w chwili odebrania informacji o podlaczeniu sie
    def connected(self,uri):
        self.conn.setText("Connected to {}".format(uri))
        print("Connected to {}".format(uri))
        self.log_thread()
        Thread(target=self.send_ctrl).start()

    # funkcja wywolywana w chwili zakonczenia transmisji
    def disconnected(self,uri):
        self.conn.setText("Disconnected")
        print("disconnected from {}".format(uri))
        self.is_connected=False

    # funkcja  konczaca polaczenie
    def close(self):
        self.cf.close_link()

    # ustawienia watku zbierajacego dane
    def log_thread(self):
        self.log = LogConfig(name="acc", period_in_ms=100)
        self.log.add_variable("acc.x", "float")
        self.log.add_variable("acc.y", "float")
        self.log.add_variable("acc.z", "float")

        try:
            self.cf.log.add_config(self.log)
            # This callback will receive the data
            self.log.data_received_cb.add_callback(self.log_received)
            # # This callback will be called on errors
            self.log.error_cb.add_callback(self.log_error)
            # Start the logging
            self.log.start()
        except KeyError as e:
            print "Could not start log configuration," \
                  "{} not found in TOC".format(str(e))
        except AttributeError:
            print "Could not add Stabilizer log config, bad configuration."

    # odbieranie danych
    def log_received(self,timestamp, data, logconf):
        # self.x.setText("x: {:.3f}".format(data["acc.x"]))
        self.y.setText("y: {:.3f}".format(data["acc.y"]))
        self.z.setText("z: {:.3f}".format(data["acc.z"]))
        # print("{}, {} = {}".format(timestamp,logconf.name,data["acc.x"]))

    def log_error(self,logconf, msg):
        print("error while loggoing {}\n{}".format(logconf.name,msg))

    # zmiana ustawien sterowania
    def update_ctrl(self,thrust):
        print("thrust changed to {}".format(thrust))
        self.thrust=thrust

    # watek wysylajacy sterowanie
    def send_ctrl(self):
        print("ctrl+send")
        pitch = 0
        roll = 0
        yawrate = 0

        while True:
            thrust=self.thrust

            if thrust > 60000:
                thrust=60000
            if thrust < 0:
                thrust=0

            #Unlock startup thrust protection
            if self.startup:
                self.cf.commander.send_setpoint(0,0,0,0)
                self.startup=False

            self.cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
            sleep(0.01)



