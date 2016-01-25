import sys
from PyQt4 import QtGui
from main_window import Ui_MainWindow
sys.path.append("../lib")
import cflib.crtp
from CF_class_imu import Crazy as cf
import usb.core
import logging
logging.basicConfig(level=logging.ERROR)
from threading import Thread
import time

class window(QtGui.QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_signals()
        self.computing=Thread(target=self.compute)



        self.cf=cf([self.ui.l_gyro_x,self.ui.l_gyro_y,self.ui.l_gyro_z],[self.ui.l_acc_x,self.ui.l_acc_y,self.ui.l_acc_z],self.ui.l_status)
    def set_signals(self):

        self.ui.pb_scan.clicked.connect(self.scan)

        self.ui.pb_conn.clicked.connect(self.pb_conn_clicked1)
        self.ui.pb_disc.clicked.connect(self.pb_disc_clicked1)

    # ustawienie polaczenie
    def pb_conn_clicked1(self):

        # self.computing.start()

        uri=self.ui.cb_device.currentText()
        self.ui.l_status.setText("connecting to {}".format(uri))
        self.cf.connect(uri)
        self.ui.pb_scan.setEnabled(False)
        self.ui.cb_device.setEnabled(False)
        self.ui.pb_disc.setEnabled(True)
        self.ui.pb_conn.setEnabled(False)

    # # rozlacznie
    def pb_disc_clicked1(self):


        self.ui.l_status.setText("Disconnecting ...")
        self.cf.close()

        self.ui.cb_device.setEnabled(True)
        self.ui.pb_disc.setEnabled(False)
        self.ui.pb_conn.setEnabled(True)

        self.ui.pb_scan.setEnabled(True)

    # funkcja wyszukiwania + wypelnienie cb
    def scan(self):
        # find USB devices
        dev = usb.core.find(find_all=True)

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

    def compute(self):
        self.roll=0
        self.pitch=0
        self.yaw=0
        x=0
        y=0
        z=0
        time.sleep(5)
        while True:
            if self.cf.is_connected:
                # print self.ui.l_acc_x.text()
                # self.convertion()
                # acc=[float(self.ui.l_acc_x.text[3:]),float(self.ui.l_acc_y.text[3:]),float(self.ui.l_acc_z.text)[3:]]
                gyro=[float(self.ui.l_acc_x.text()[3:]),float(self.ui.l_acc_y.text()[3:]),float(self.ui.l_acc_z.text()[3:])]
                self.roll+=gyro[0]/ 100.0
                self.pitch+=gyro[1]/ 100.0
                self.yaw+=gyro[2]/ 100.0
                self.update_gui()
                time.sleep(0.1)


    def update_gui(self):
        self.ui.l_pitch.setText("Pitch: {:.3f}".format(self.pitch))
        self.ui.l_roll.setText("Roll: {:.3f}".format(self.roll))
        self.ui.l_yaw.setText("Pitch: {:.3f}".format(self.yaw))



def main():
    app = QtGui.QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    cflib.crtp.init_drivers(enable_debug_driver=False)
    main()

