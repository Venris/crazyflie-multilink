import sys
from time import sleep
from PyQt4 import QtGui
from gui.main_window4 import Ui_MainWindow
import zmq
from threading import Thread
from math import cos, sin, pi
sys.path.append("../lib")
import cflib.crtp
from CF_class_sterowanie2 import Crazy as cf
import usb.core
import logging
logging.basicConfig(level=logging.ERROR)
# from sterowanie.fuzzy import fuzzy_ctrl as control
from sterowanie.sprzezenie import control
import pyqtgraph as pg
import numpy as np
from sterowanie.fuzzy import fuzzyZ as fz


class window(QtGui.QMainWindow):

    def __init__(self,app):
        super(window, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.app=app
        self.set_signals()
        self.update_target()
        zmq=Thread(target=self.run_zmq)
        zmq.daemon=True
        zmq.start()
        self.rpy=[0,0,0]
        self.cf=cf(self.ui,self.rpy)
        self.init_var()
        self.init_plot()
        self.scan()

    def init_plot(self):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.ui.plot_widget=pg.PlotWidget(name="plot1")
        self.ui.plot_layout.addWidget(self.ui.plot_widget)
        self.ui.plot_widget.setLabel('left', 'Value')
        self.ui.plot_widget.setLabel('bottom', 'Time', units='s')
        self.plot=self.ui.plot_widget.plot()
        self.update_plot_thread=Thread(target=self.update_plot)
        self.update_plot_thread.daemon=True
        self.update_plot_thread.start()
        self.can_update=True



    def update_plot(self):

        while True:
            if len(self.x_plot)>0 and self.can_update:
                self.plot.setData(y=self.y_plot,x=self.x_plot)
                sleep(0.1)







    def init_var(self):
        self.z=0
        self.x=0
        self.y=0
        self.theta=0

        self.Vz=0
        self.Vx=0
        self.Vy=0
        self.Vtheta=0

        self.x_d = 0
        self.y_d = 0
        self.Vx_d = 0
        self.Vy_d = 0

        self.x_plot=[]
        self.y_plot=[]

    def set_signals(self):
        self.ui.pb_scan.clicked.connect(self.scan)
        self.ui.pb_conn.clicked.connect(self.pb_conn_clicked)
        self.ui.pb_disc.clicked.connect(self.pb_disc_clicked)
        self.ui.pb_start.clicked.connect(self.pb_start_clicked)
        self.ui.pb_stop.clicked.connect(self.pb_stop_clicked)
        self.ui.pb_update.clicked.connect(self.update_target)

        self.app.aboutToQuit.connect(self.exit)

    def exit(self):
        self.ctrl_isTrue=False
        self.cf.close()


    # ustawienie polaczenie
    def pb_conn_clicked(self):
        uri=self.ui.cb_device.currentText()
        self.ui.l_conn.setText("connecting to {}".format(uri))
        self.cf.connect(uri)
        self.ui.pb_scan.setEnabled(False)
        self.ui.pb_conn.setEnabled(False)
        self.ui.cb_device.setEnabled(False)
        self.ui.pb_disc.setEnabled(True)

        self.ui.gb_target.setEnabled(True)
        self.ui.gb_control.setEnabled(True)

    # rozlacznie
    def pb_disc_clicked(self):
        # self.pb_stop_clicked()
        self.ui.l_conn.setText("Disconnecting ...")
        self.cf.close()

        self.ui.pb_scan.setEnabled(True)
        self.ui.cb_device.setEnabled(True)
        self.ui.pb_disc.setEnabled(False)

        self.ui.gb_target.setEnabled(False)
        self.ui.gb_control.setEnabled(False)


    # sterowanie
    def pb_start_clicked(self):
        self.ui.pb_start.setEnabled(False)
        self.ui.pb_stop.setEnabled(True)
        self.ui.pb_update.setEnabled(True)
        self.ui.pb_disc.setEnabled(False)
        self.update_target();

        self.ctrl_isTrue=True
        self.ctrl_thread=Thread(target=self.ctrl)
        self.ctrl_thread.daemon=True
        self.ctrl_thread.start()


    def pb_stop_clicked(self):
        self.ui.pb_start.setEnabled(True)
        self.ui.pb_stop.setEnabled(False)
        # self.ui.pb_update.setEnabled(False)
        self.ui.pb_disc.setEnabled(True)
        self.ctrl_isTrue=False
        # sleep(0.1)
        self.ctrl_thread.join()


    def update_target(self):
        self.x_t=float(self.ui.en_x.text())
        self.y_t=float(self.ui.en_y.text())
        self.z_t=float(self.ui.en_z.text())
        self.theta_t=float(self.ui.en_theta.text())

        self.x_d_t=self.x_t*cos(self.theta_t*pi/180)-self.y_t*sin(self.theta_t*pi/180)
        self.y_d_t=self.x_t*sin(self.theta_t*pi/180)+self.y_t*cos(self.theta_t*pi/180)

    def ctrl(self):
        self.x_plot=np.array([0.0])
        self.y_plot=np.array([0.0])
        timeout=0

        thrust_p=0
        roll_p=0
        pitch_p=0
        yaw_p=0

        while self.ctrl_isTrue:

            if (self.x==5 or self.y==5 or self.z==5) :
                thrust=thrust_p
                roll=roll_p
                pitch=pitch_p
                yaw=yaw_p
                timeout+=1
                if timeout>=20:
                    self.ctrl_isTrue=False
                    break

            elif (self.x==0 and self.y==0 and self.z==0 and self.theta==0):
                thrust=0
                roll=-4
                pitch=0
                yaw=0

            else:
                thrust=fz(self.z_t-self.z,self.Vz)
                roll=0
                pitch=0
                yaw=0
                timeout=0


            self.ui.l_thrust.setText("Thrust: {}".format(thrust))
            self.ui.l_roll.setText("roll: {}".format(roll))
            self.ui.l_pitch.setText("pitch: {}".format(pitch))
            self.ui.l_yaw.setText("yaw: {}".format(yaw))

            self.cf.update_ctrl(thrust*600,pitch,roll,yaw)

            self.save_plot_data(self.x_plot[-1]+0.05,self.rpy[2])

            sleep(0.05)
        self.cf.update_ctrl(0,0,0,0)
        self.ui.l_thrust.setText("Thrust: {:f}".format(0))
        self.ui.l_roll.setText("roll: {:f}".format(0))
        self.ui.l_pitch.setText("pitch: {:f}".format(0))
        self.ui.l_yaw.setText("yaw: {:f}".format(0))


    def save_plot_data(self,xdata,ydata):
        self.can_update=False
        self.x_plot=np.append(self.x_plot,xdata)
        self.y_plot=np.append(self.y_plot,ydata)
        if len(self.x_plot)>100 or len(self.y_plot)>100 :

            self.x_plot=np.delete(self.x_plot,0)
            self.y_plot=np.delete(self.y_plot,0)
        self.can_update=True


    # funkcja wyszukiwania + wypelnienie cb
    def scan(self):
        # find USB devices
        dev = usb.core.find(find_all=True)
        try:
            a=cflib.crtp.scan_interfaces()
            self.ui.cb_device.clear()
            k=0
            kk=0
            for cfg in dev:
                if cfg.idVendor==6421:
                    for i in a:
                        self.ui.cb_device.addItem(i[0].replace(str(kk),str(k),1))
                    kk=k
                    k+=1
            if len(a)>0:
                self.ui.pb_conn.setEnabled(True)
            else:
                self.ui.pb_conn.setEnabled(False)
        except Exception as e:
            self.ui.l_conn.setText(str(e))

    def run_zmq(self):
        port=2500
        context = zmq.Context()
        print "Connecting to server..."
        socket = context.socket(zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE, u"")
        socket.connect ("tcp://192.168.2.103:%s" % port)
        # socket.connect ("tcp://localhost:%s" % port)

        while True:
            rcv=socket.recv_unicode()
            # rcv=str(rcv)
            if rcv!=None and len(rcv)>0:
                rcv=rcv.replace(",",".")
                splited=rcv.split(";")
                if self.x!=5 and self.y!=5 and self.z!=5 and self.theta!=200:
                    self.x_p=self.x
                    self.y_p=self.y
                    self.z_p=self.z
                    self.theta_p=self.theta
                    self.x_d_p=self.x_d
                    self.y_d_p=self.y_d


                self.x=float(splited[0])
                self.y=float(splited[1])
                self.z=float(splited[2])
                self.theta=float(splited[3])

                self.Vx=self.x-self.x_p
                self.Vy=self.y-self.y_p
                self.Vz=self.z-self.z_p
                self.Vtheta=self.theta-self.theta_p


                self.x_d=self.x*cos(self.theta*pi/180)-self.y*sin(self.theta*pi/180)
                self.y_d=self.x*sin(self.theta*pi/180)+self.y*cos(self.theta*pi/180)

                self.Vx_d=self.x_d-self.x_d_p
                self.Vy_d=self.y_d-self.y_d_p


                # self.x_e=float(splited[0])-self.x_t
                # self.y_e=float(splited[1])-self.y_t
                # self.z_e=float(splited[2])-self.z_t
                # self.theta_e=float(splited[3])-self.theta_t

                # wyswietlanie na gui
                self.ui.l_x.setText("x: {}".format(splited[0]))
                self.ui.l_y.setText("y: {}".format(splited[1]))
                self.ui.l_z.setText("z: {}".format(splited[2]))
                self.ui.l_theta.setText("kat: {}".format(splited[3]))

                self.ui.l_vx.setText("x: {}".format(self.Vx))
                self.ui.l_vy.setText("y: {}".format(self.Vy))
                self.ui.l_vz.setText("z: {}".format(self.Vz))
                self.ui.l_vtheta.setText("kat: {}".format(self.Vtheta))



            # sleep(0.01)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = window(app)

    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    cflib.crtp.init_drivers(enable_debug_driver=False)
    main()

