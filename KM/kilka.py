import sys
from time import sleep

sys.path.append('../lib')
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cfclient.utils.logconfigreader import LogConfig
from threading import Thread, Timer
import logging

logging.basicConfig(level=logging.ERROR)


class MyCF:
    def __init__(self, uri):
        self.cf = Crazyflie()
        self.cf.connected.add_callback(self.connected)
        self.cf.disconnected.add_callback(self.disconnected)
        self.cf.open_link(uri)
        self.uri = uri

        self.is_connected = False

    def connected(self, uri):
        self.is_connected = True
        print("Connected to {}".format(uri))

    def disconnected(self, uri):
        print("disconnected from {}".format(uri))

    def close(self):
        self.cf.close_link()

    def start_motors(self):
        Thread(target=self.motor).start()

    def motor(self):
        thrust_mult = 1
        thrust_step = 200
        thrust = 20000
        pitch = 0
        roll = 0
        yawrate = 0

        # Unlock startup thrust protection
        self.cf.commander.send_setpoint(0, 0, 0, 0)

        while thrust >= 15000:
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
    a = cflib.crtp.scan_interfaces()

    for i in a:
        print(i)

    liczba_dronow = int(input("podaj liczbe dronow: "))
    cf = []
    for i in range(liczba_dronow):
        nr = input("wybierz uri drona nr {}: ".format(i))
        cf.append(MyCF(a[nr][0]))


    while any(item.is_connected==False for item in cf):
        sleep(0.5)

    for i in cf:
        i.start_motors()

    test=raw_input("press any key...")

    for i in cf:
        i.close()
    # trigger=True
    #
    #     while trigger:
    #         for i in cf:




