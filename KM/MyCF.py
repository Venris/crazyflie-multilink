import sys
from time import sleep
sys.path.append('../lib')
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cfclient.utils.logconfigreader import LogConfig
from threading import Thread,Timer


import logging
logging.basicConfig(level=logging.ERROR)

class MyCF:
    def __init__(self,uri):
        self.cf=Crazyflie()
        self.cf.connected.add_callback(self.connected)
        self.cf.disconnected.add_callback(self.disconnected)
        self.cf.open_link(uri)
        self.uri=uri

        self.is_connected=True

    def connected(self,uri):
        print("Connected to {}".format(uri))
        # Thread(target=self.motor).start()
        self.log_thread()

    def disconnected(self,uri):
        print("disconnected from {}".format(uri))

    def close(self):
        self.cf.close_link()

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

        t=Timer(5,self.close)

    def log_received(self,timestamp, data, logconf):
        # self.x.setText("x: {}".format["acc.x"])
        # self.y.setText("y: {}".format["acc.y"])
        # self.z.setText("z: {}".format["acc.z"])
        print("{}, {} = {} on {}".format(timestamp,logconf.name,data["acc.x"],self.uri))


    def log_error(self,logconf, msg):
        print("error while loggoing {}\n{}".format(logconf.name,msg))


    def motor(self):
        thrust_mult = 1
        thrust_step = 50
        thrust = 20000
        pitch = 0
        roll = 0
        yawrate = 0

        #Unlock startup thrust protection
        self.cf.commander.send_setpoint(0, 0, 0, 0)



        while thrust >= 20000:
            self.cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
            sleep(0.1)
            if thrust >= 25000:
                thrust_mult = -1
            thrust += thrust_step * thrust_mult
        self.cf.commander.send_setpoint(0, 0, 0, 0)
        # Make sure that the last packet leaves before the link is closed
        # since the message queue is not flushed before closing
        sleep(0.1)
        self.close()


if __name__ == "__main__":
    cflib.crtp.init_drivers(enable_debug_driver=False)
    a=cflib.crtp.scan_interfaces()
    b=cflib.crtp.get_interfaces_status()
    for i in a:
        print(i)

    for i in b:
        print (i)

    # uri1=int(input("1:"))-1
    # uri2=int(input("2:"))-1

    cf1=MyCF('radio://0/40/1M')#(a[uri1][0])
    # sleep(1)
    # cf2=MyCF('radio://1/40/1M')#a[uri2][0])


    sleep(5)
    cf1.close()
    # cf2.close()



