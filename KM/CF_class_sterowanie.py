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
    def __init__(self,ui):

        # zmienne pomocnicze w obsludze GUI
        self.ui=ui

        self.thrust=0
        self.pitch=0
        self.roll=0
        self.yaw=0
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
        self.ui.l_conn.setText("Connected to {}".format(uri))
        print("Connected to {}".format(uri))
        control=Thread(target=self.send_ctrl)
        control.start()
        # self.log_thread()

    # funkcja wywolywana w chwili zakonczenia transmisji
    def disconnected(self,uri):
        self.ui.l_conn.setText("Disconnected")
        print("disconnected from {}".format(uri))
        self.is_connected=False

    # funkcja  konczaca polaczenie
    def close(self):
        self.cf.close_link()

    # ustawienia watku zbierajacego dane
    def log_thread(self):
        self.log = LogConfig(name="logs", period_in_ms=100)
        self.log.add_variable("stabilizer.roll", "float")
        self.log.add_variable("stabilizer.pitch", "float")
        self.log.add_variable("stabilizer.yaw", "float")

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
        self.katy[0]=data["stabilizer.roll"]
        self.katy[1]=data["stabilizer.pitch"]
        self.katy[2]=data["stabilizer.yaw"]
        self.ui.l_pitch_a.setText("Pitch: {:.3f}".format(self.katy[1]))
        self.ui.l_roll_a.setText("Roll: {:.3f}".format(self.katy[0]))
        self.ui.l_yaw_a.setText("Yaw: {:.3f}".format(self.katy[2]))
        # print("{}, {} = {}".format(timestamp,logconf.name,data["acc.x"]))

    def log_error(self,logconf, msg):
        print("error while loggoing {}\n{}".format(logconf.name,msg))

    # zmiana ustawien sterowania
    def update_ctrl(self,thrust,pitch,roll,yaw):
        print("thrust changed to {}".format(thrust))
        print("yaw changed to {}".format(yaw))
        print("pitch changed to {}".format(pitch))
        print("roll changed to {}".format(roll))
        self.thrust=thrust
        self.pitch=pitch
        self.roll=roll
        self.yaw=yaw


    # watek wysylajacy sterowanie
    def send_ctrl(self):

        while True:


            if self.thrust > 60000:
                self.thrust=60000
            if self.thrust < 0:
                self.thrust=0

            #Unlock startup thrust protection
            if self.startup:
                self.cf.commander.send_setpoint(0,0,0,0)
                self.startup=False

            self.cf.commander.send_setpoint(self.roll, self.pitch, self.yaw, self.thrust)
            sleep(0.01)



