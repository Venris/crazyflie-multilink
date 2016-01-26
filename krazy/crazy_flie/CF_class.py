import sys
from time import sleep
sys.path.append('../lib')
from cflib.crazyflie import Crazyflie
from cfclient.utils.logconfigreader import LogConfig
from threading import Thread
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import QObject
import logging
logging.basicConfig(level=logging.ERROR)

class Crazy(QObject):
    cf_connected=pyqtSignal(bool)
    cf_logs=pyqtSignal(dict)
    def __init__(self,parent):
        super(Crazy, self).__init__()

        # zmienne pomocnicze w obsludze GUI
        self.thrust=0
        self.pitch=0
        self.roll=0
        self.yaw=0
        self.startup=True
        self.is_connected=False
        self.busy=False

        self.control_started=False


        # zmienna do wysylania logow
        self.log_data={"roll":0.0,"pitch":0.0,"yaw":0.0,"thrust":0.0,"m1":0.0,"m2":0.0,"m3":0.0,"m4":0.0}

        # ustawienia dobierania danych do sterowania
        parent.control_data_sig.connect(self.update_ctrl_sig)

        # ustawienia biblioteki cf
        self.cf=Crazyflie()
        self.cf.connected.add_callback(self.connected)
        self.cf.disconnected.add_callback(self.disconnected)
        self.cf.connection_lost.add_callback(self.lost_connection)

        #ustawienie watku sterowania
        self.control=Thread(target=self.send_ctrl)

    #funkcja inicjujaca polaczenie
    def connect(self,uri):
        self.cf.open_link(uri)


    # funkcja wywolywana w chwili odebrania informacji o podlaczeniu sie
    def connected(self,uri):
        self.is_connected=True


        print("Connected to {}".format(uri))
        self.log_thread()
        self.cf_connected.emit(self.is_connected)
        self.control.start()
        self.control_started=True


    # funkcja wywolywana w chwili zakonczenia transmisji
    def disconnected(self,uri):
        print("disconnected from {}".format(uri))
        self.is_connected=False
        self.cf_connected.emit(self.is_connected)
        if self.control_started:
            self.control.join(0.1)

    def lost_connection(self,uri,var):
        print("disconnected from {}".format(uri))
        self.is_connected=False
        self.cf_connected.emit(self.is_connected)
        if self.control_started:
            self.control.join(0.1)
        self.close()


    # funkcja  konczaca polaczenie
    def close(self):
        self.cf.close_link()

    # ustawienia watku zbierajacego dane
    def log_thread(self):
        print "test"
        self.log = LogConfig(name="logs", period_in_ms=10)
        self.log.add_variable("stabilizer.roll", "float")
        self.log.add_variable("stabilizer.pitch", "float")
        self.log.add_variable("stabilizer.yaw", "float")
        # self.log.add_variable("stabilizer.thrust", "float")
        # self.log.add_variable("motor.m1", "float")
        # self.log.add_variable("motor.m2", "float")
        # self.log.add_variable("motor.m3", "float")
        # self.log.add_variable("motor.m4", "float")


        try:
            print "test 2"
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
        # print"log"
        try:
            self.log_data["roll"]=data["stabilizer.roll"]
            self.log_data["pitch"]=data["stabilizer.pitch"]
            self.log_data["yaw"]=data["stabilizer.yaw"]
            # self.log_data["thrust"]=data["stabilizer.thrust"]
            # self.log_data["m1"]=data["motor.m1"]
            # self.log_data["m2"]=data["motor.m2"]
            # self.log_data["m3"]=data["motor.m3"]
            # self.log_data["m4"]=data["motor.m4"]
        except:
            print("blad logowania")

        self.cf_logs.emit(self.log_data)
        # print (self.log_data)
    def log_error(self,logconf, msg):
        ("error while loggoing {}\n{}".format(logconf.name,msg))

    # zmiana ustawien sterowania
    def update_ctrl(self,thrust,pitch,roll,yaw):
        # ("thrust | pitch | roll | yaw ")
        self.busy=True
        # ("{:.3f} | {:.3f} | {:.3f} | {:.3f}".format(thrust,pitch,roll,yaw))
        self.thrust=thrust
        self.pitch=pitch
        self.roll=roll
        self.yaw=yaw
        self.busy=False

    def update_ctrl_sig(self,data):
        # self.busy=True
        # print("{:.3f} | {:.3f} | {:.3f} | {:.3f}".format(data["thrust"],data["pitch"],data["roll"],data["yaw"]))
        self.thrust=data["thrust"]
        self.pitch=data["pitch"]
        self.roll=data["roll"]
        self.yaw=data["yaw"]
        # self.busy=False


    # watek wysylajacy sterowanie
    def send_ctrl(self):

        while self.is_connected:
            if not self.busy:
                if self.thrust > 60000:
                    self.thrust=60000
                if self.thrust < 0:
                    self.thrust=0
                #Unlock startup thrust protection
                if self.startup:
                    self.cf.commander.send_setpoint(0,0,0,0)
                    self.startup=False
                # self.cf.commander.set_client_xmode(False)
                self.cf.commander.send_setpoint(self.roll, self.pitch, self.yaw, self.thrust)

                sleep(0.01)



