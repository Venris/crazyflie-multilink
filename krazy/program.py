from gui.main_window import Ui_MainWindow
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal
from crazy_flie.dron_class import dron
import usb.core
import sys
import logging
logging.basicConfig(level=logging.ERROR)
sys.path.append("../lib")
import cflib.crtp
import zmq
from zmq_fun.zmq_thread import zmq_thread
from math import cos,pi,sin



class main_window(QtGui.QMainWindow):

    def __init__(self,app,socket):
        # ustawienia podstawowe
        super(main_window, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.app=app

        # wlaczenie watku zmq
        self.zmq = zmq_thread(socket)
        self.zmq.start()



        # ustawinie sygnalow
        self.setup_signals()

        #inicjalizacja zmiennych
        self.dron_list=[]
        self.row=0
        self.column=0

        self.scan_devices()
        # self.add_dron()

    def setup_signals(self):
        self.ui.pb_add_dron.clicked.connect(self.add_dron)
        self.ui.pb_remove.clicked.connect(self.remove_drons)
        self.ui.pb_scan_devices.clicked.connect(self.scan_devices)

        self.zmq.zmq_log.connect(self.zmq_log_recv)

        self.app.aboutToQuit.connect(self.remove_drons)

    def zmq_log_recv(self,data):
        number=5
        dt=data[-1]
        data=data[:-1]
        # print len(self.dron_list)
        if len(self.dron_list)>0:
            for dron in self.dron_list:
                dron.dt=dt

                dron.isCorrect=data[0+number*dron.id]
                # print type(dron.isCorrect)
                dron.x_cam=data[1+number*dron.id]/100.0
                dron.y_cam=data[2+number*dron.id]/100.0
                dron.z_cam=data[3+number*dron.id]/100.0
                dron.yaw_cam=data[4+number*dron.id]*pi/180
                dron.vzcam=(dron.z_cam-dron.z_cam_p)/dt
                dron.z_cam_p=dron.z_cam


                if dron.isCorrect==1.0:

                    pass

                else:
                    pass
                    # dron.x_cam=dron.x_previous
                    # dron.y_cam=dron.y_previous
                    # dron.z_cam=dron.z_previous
                    # dron.yaw_cam=dron.yaw_previous






    def scan_devices(self):
        dev = usb.core.find(find_all=True)
        try:
            a=cflib.crtp.scan_interfaces()
            self.ui.cb_devices.clear()
            k=0
            kk=0
            for cfg in dev:
                if cfg.idVendor==6421:
                    for i in a:
                        self.ui.cb_devices.addItem(i[0].replace(str(kk),str(k),1))
                    kk=k
                    k+=1
        except Exception as e:
            print e

    def add_dron(self):
        number_of_drons=(len(self.dron_list))
        uri=self.ui.cb_devices.currentText()
        if uri!=None and uri!="":
            self.ui.cb_devices.removeItem(self.ui.cb_devices.currentIndex())
            if number_of_drons<4:
                self.dron_list.append(dron(int(self.ui.en_id.text()),uri,self))
                self.ui.en_id.setText(str(number_of_drons+1))
                self.ui.layout_drons.addWidget(self.dron_list[-1],self.row,self.column)
                self.row+=1
                if self.row>=2:
                    self.row=0
                    self.column+=1

    def remove_drons(self):
        self.row=0
        self.column=0
        for dron in self.dron_list:
            dron.cf.close()
            dron.deleteLater()

        self.dron_list=[]







if __name__=="__main__":
    cflib.crtp.init_drivers(enable_debug_driver=False)
    port=2500
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, u"")
    socket.connect ("tcp://192.168.2.109:%s" % port)
    # socket.connect ("tcp://localhost:%s" % port)


    app = QtGui.QApplication(sys.argv)
    ex = main_window(app,socket)
    ex.show()
    # ex.showMaximized()
    sys.exit(app.exec_())

