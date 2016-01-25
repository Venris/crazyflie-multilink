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
    def __init__(self,l_gyro,l_acc,l_status):

        # zmienne pomocnicze w obsludze GUI
        self.conn=l_status
        self.l_gyro=l_gyro
        self.l_acc=l_acc
        self.is_connected=False
        self.r=0
        self.p=0
        self.y=0

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

        self.log_acc = LogConfig(name="acc", period_in_ms=100)
        self.log_acc.add_variable("acc.x", "float")
        self.log_acc.add_variable("acc.y", "float")
        self.log_acc.add_variable("acc.z", "float")

        self.log_acc.add_variable("gyro.x", "float")
        self.log_acc.add_variable("gyro.y", "float")
        self.log_acc.add_variable("gyro.z", "float")

        try:
            self.cf.log.add_config(self.log_acc)

            # This callback will receive the data
            self.log_acc.data_received_cb.add_callback(self.log_received_acc)

            # # This callback will be called on errors
            self.log_acc.error_cb.add_callback(self.log_error)

            # Start the logging
            self.log_acc.start()
        except KeyError as e:
            print "Could not start log configuration," \
                  "{} not found in TOC".format(str(e))
        except AttributeError:
            print "Could not add Stabilizer log config, bad configuration."

    # odbieranie danych
    def log_received_acc(self,timestamp, data, logconf):
        rate=0.1
        self.r+=data['gyro.x']*rate
        self.p+=data['gyro.y']*rate
        self.y+=data['gyro.z']*rate


        self.l_acc[0].setText("roll: {:.3f}".format(self.r))
        self.l_acc[1].setText("pitch: {:.3f}".format(self.p))
        self.l_acc[2].setText("yaw: {:.3f}".format(self.y))
        self.l_gyro[0].setText("x: {:.3f}".format(data["gyro.x"]))
        self.l_gyro[1].setText("y: {:.3f}".format(data["gyro.y"]))
        self.l_gyro[2].setText("z: {:.3f}".format(data["gyro.z"]))
        # print("{}, {} = {}".format(timestamp,logconf.name,data["acc.x"]))



    def log_error(self,logconf, msg):
        print("error while loggoing {}\n{}".format(logconf.name,msg))




