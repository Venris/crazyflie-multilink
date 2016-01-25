import sys
from PyQt4 import QtGui
from gui.main_window import Ui_MainWindow
sys.path.append("../lib")
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cfclient.utils.logconfigreader import LogConfig
from CF_class import Crazy as cf
import usb.core
import logging
logging.basicConfig(level=logging.ERROR)
from threading import Thread
import camera


class window(QtGui.QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_signals()
        Thread(target=self.pozycja).start()



        self.cf1=cf(self.ui.l_x1,self.ui.l_y1,self.ui.l_z1,self.ui.l_conn1)
        self.cf2=cf(self.ui.l_x2,self.ui.l_y2,self.ui.l_z2,self.ui.l_conn2)


    def set_signals(self):
        self.ui.pb_scan.clicked.connect(self.scan)

        self.ui.pb_conn1.clicked.connect(self.pb_conn_clicked1)
        self.ui.pb_conn2.clicked.connect(self.pb_conn_clicked2)

        self.ui.pb_disc1.clicked.connect(self.pb_disc_clicked1)
        self.ui.pb_disc2.clicked.connect(self.pb_disc_clicked2)

        self.ui.pb_send1.clicked.connect(self.pb_send_clicked1)
        self.ui.pb_send2.clicked.connect(self.pb_send_clicked2)
    # ustawienie polaczenie
    def pb_conn_clicked1(self):
        uri=self.ui.cb_device1.currentText()
        self.ui.l_conn1.setText("connecting to {}".format(uri))
        self.cf1.connect(uri)
        self.ui.pb_scan.setEnabled(False)
        self.ui.cb_device1.setEnabled(False)
        self.ui.pb_disc1.setEnabled(True)
        self.ui.pb_send1.setEnabled(True)
        self.ui.pb_conn1.setEnabled(False)
        self.ui.e_thrust1.setEnabled(True)
    def pb_conn_clicked2(self):
        uri=self.ui.cb_device2.currentText()
        self.ui.l_conn2.setText("connecting to {}".format(uri))
        self.cf2.connect(uri)
        self.ui.pb_scan.setEnabled(False)
        self.ui.cb_device2.setEnabled(False)
        self.ui.pb_disc2.setEnabled(True)
        self.ui.pb_send2.setEnabled(True)
        self.ui.pb_conn2.setEnabled(False)
        self.ui.e_thrust2.setEnabled(True)
    # # rozlacznie
    def pb_disc_clicked1(self):
        self.ui.l_conn1.setText("Disconnecting ...")
        self.cf1.close()

        self.ui.cb_device1.setEnabled(True)
        self.ui.pb_disc1.setEnabled(False)
        self.ui.pb_send1.setEnabled(False)
        self.ui.pb_conn1.setEnabled(True)
        self.ui.e_thrust1.setEnabled(False)

        if self.cf2.is_connected:
            self.ui.pb_scan.setEnabled(False)
        else:
            self.ui.pb_scan.setEnabled(True)
    def pb_disc_clicked2(self):
        self.ui.l_conn2.setText("Disconnecting ...")
        self.cf2.close()

        self.ui.cb_device2.setEnabled(True)
        self.ui.pb_disc2.setEnabled(False)
        self.ui.pb_send2.setEnabled(False)
        self.ui.pb_conn2.setEnabled(True)
        self.ui.e_thrust2.setEnabled(False)

        if self.cf1.is_connected:
            self.ui.pb_scan.setEnabled(False)
        else:
            self.ui.pb_scan.setEnabled(True)
    # wyslanie nowego sterowania
    def pb_send_clicked1(self):
        thrust=int(self.ui.e_thrust1.text())
        if thrust > 100:
            thrust=100
        if thrust < 0:
            thrust=0

        self.ui.e_thrust1.clear()
        self.ui.e_thrust1.setText(str(thrust))

        thrust=thrust*500
        self.cf1.update_ctrl(thrust)
    def pb_send_clicked2(self):
        thrust=int(self.ui.e_thrust2.text())
        if thrust > 100:
            thrust=100
        if thrust < 0:
            thrust=0

        self.ui.e_thrust2.clear()
        self.ui.e_thrust2.setText(str(thrust))

        thrust=thrust*500
        self.cf2.update_ctrl(thrust)
    # funkcja wyszukiwania + wypelnienie cb
    def scan(self):
        # find USB devices
        dev = usb.core.find(find_all=True)


        a=cflib.crtp.scan_interfaces()
        self.ui.cb_device1.clear()
        self.ui.cb_device2.clear()

        k=0
        kk=0
        for cfg in dev:
            if cfg.idVendor==6421:
                for i in a:
                    self.ui.cb_device1.addItem(i[0].replace(str(kk),str(k),1))
                    self.ui.cb_device2.addItem(i[0].replace(str(kk),str(k),1))
                kk=k
                k+=1
        if len(a)>0:
            self.ui.pb_conn1.setEnabled(True)
            self.ui.pb_conn2.setEnabled(True)
        else:
            self.ui.pb_conn1.setEnabled(False)
            self.ui.pb_conn2.setEnabled(False)

    def pozycja(self):
        x,y=camera.wykrywanie()
        self.ui.l_x1.setText(str(x))
        self.ui.l_x2.setText(str(y))

def main():
    app = QtGui.QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    cflib.crtp.init_drivers(enable_debug_driver=False)
    main()

