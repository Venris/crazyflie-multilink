from dron import Ui_Dron
from PyQt4 import QtGui
from CF_class import Crazy as cf
from PyQt4.QtCore import pyqtSignal,QTimer
from math import cos,sin,pi
from fuzzy import fuzzyKat as fyaw, fuzzyX as fx, fuzzyY as fy,fuzzyZ as fz, fuzzydron as fd
from lqr import control
import time
from control import controlData
from PID import PID
import numpy as np
from kalman import kalman12
import sprzezenie
class dron(QtGui.QWidget):
    control_data_sig=pyqtSignal(dict)
    def __init__(self,id,uri,parent):
        super(dron, self).__init__()
        # ustawienie gui
        self.ui=Ui_Dron()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(1)
        # time.sleep(1)
        # self.ui.tabWidget.setCurrentIndex(0)

        #ustawienia drona
        self.uri=uri
        self.id=id
        self.cf=cf(self)
        self.ui.l_conn.setText("Choosen: {}".format(self.uri))

        # odswiezanie interfejsu
        self.update_gui_thread=QTimer()
        self.update_gui_thread.timeout.connect(self.update_interface)
        self.update_gui_thread.start(100)

        # liczenie sterowania
        self.update_control_thread=QTimer()
        self.update_control_thread.timeout.connect(self.update_control)
        self.timeout=0



        self.set_signals()
        self.set_variables()

    def set_variables(self):
        # inicjalizacja filtru kalmana
        self.kalman=kalman12()
        self.z_cam_p=0
        self.vzcam=0

        # inicjalizacja danych zmq
        # pozycje
        self.strlist=[]
        self.strlist.append("x,y,z,yaw,vzcam,xk,yk,zk,rollk,pitchk,yawk,vxk,vyk,vzk,vrollk,vpitchk,vyawk,pitch_con,roll_con,yaw_con,thrust_cam,xd,yd,zd,rolld,pitchd,yawd")

        self.stan=np.zeros((1,8))
        self.isCorrect="0"

        self.x_cam=0
        self.y_cam=0
        self.z_cam=0
        self.yaw_cam=0
        self.dt=-1



        # x,y w ukladzie drona
        self.x_dron=0
        self.y_dron=0
        self.z_dron=0

        self.x_dron_target=0
        self.y_dron_target=0
        self.z_dron_target=0

        self.vx_dron=0
        self.vy_dron=0
        self.vz_dron=0


        self.alfa_dron=0
        self.valfa_dron=0

        self.thrust_dron=0
        self.roll_dron=0
        self.pitch_dron=0
        self.yaw_dron=0
        self.vyaw_dron=0

        # inicjalizacja zmiennych do sterowania
        self.thrust_control=0.0
        self.pitch_control=0.0
        self.roll_control=0.0
        self.yaw_control=0.0

        self.thrust_control_previous=0.0
        self.pitch_control_previous=0.0
        self.roll_control_previous=0.0
        self.yaw_control_previous=0.0

        self.control_package={
            "thrust":self.thrust_control,
            "pitch":self.pitch_control,
            "roll":self.roll_control,
            "yaw":self.yaw_control
        }

        # inicjalizacja celu
        self.x_target=0.0
        self.y_target=0.4
        self.z_target=0.0
        self.yaw_target=0.0

        self.ctrl_isTrue=False


        self.daneX=controlData()
        self.daneX.K=10.0
        # self.daneX.Ti=0.1
        self.daneX.Td=0.15
        self.daneX.calka_max=1.0
        self.daneX.u_min=-10
        self.daneX.u_max=10

        self.daneY=controlData()
        self.daneY.K=10.0
        # self.daneY.Ti=0.1
        self.daneY.Td=0.15
        self.daneY.calka_max=1.0
        self.daneY.u_min=-10
        self.daneY.u_max=10

        self.daneZ=controlData()
        self.daneZ.K=50
        self.daneZ.Ti=0.1
        self.daneZ.Td=53
        self.daneZ.calka_max=1
        self.daneZ.u_min=50
        self.daneZ.u_max=80
        self.daneZ.FF=60

        self.daneTheta=controlData()
        self.daneTheta.K=1.0
        # self.daneTheta.Ti=0.1
        self.daneTheta.Td=0.15
        self.daneTheta.calka_max=1.0
        self.daneTheta.u_max=20
        self.daneTheta.u_min=-20

        self.m1=0.0
        self.m2=0.0
        self.m3=0.0
        self.m4=0.0


    def set_signals(self):
        self.ui.pb_conn_2.clicked.connect(self.connect_clicked)
        self.ui.pb_disc_2.clicked.connect(self.disconnect_clicked)
        self.ui.pb_start_2.clicked.connect(self.start_clicked)
        self.ui.pb_stop_2.clicked.connect(self.stop_clicked)
        self.ui.pb_update_2.clicked.connect(self.update_clicked)

        self.ui.pb_save.clicked.connect(self.saveFile)


        self.cf.cf_connected.connect(self.connected)
        self.cf.cf_logs.connect(self.log_recv)


    def saveFile(self):
        txt="\n".join(self.strlist)
        f=open(name="log.csv",mode='w')
        f.write(txt)
        f.close()
        del self.strlist[1:]
        print self.strlist
        print("saved")

    def log_recv(self,data):
        # print('log rcv')
        self.thrust_dron=data["thrust"]
        self.roll_dron=data["roll"]
        self.pitch_dron=data["pitch"]
        self.yaw_dron=data["yaw"]
        self.m1=data["m1"]
        self.m2=data["m2"]
        self.m3=data["m3"]
        self.m4=data["m4"]


    def connected(self,status):
            if status:
                self.ui.l_conn.setText("Connected to {}".format(self.uri))
                self.ui.pb_conn_2.setEnabled(False)
                self.ui.pb_disc_2.setEnabled(True)
                self.ui.gb_control_2.setEnabled(True)
                self.ui.pb_start_2.setEnabled(True)
                self.ui.pb_update_2.setEnabled(True)
            else:
                self.ui.l_conn.setText("Disconnected")
                self.ui.pb_conn_2.setEnabled(True)
                self.ui.pb_disc_2.setEnabled(False)
                self.ui.gb_control_2.setEnabled(False)

    def disconnect_clicked(self):
        self.cf.close()
        self.stop_clicked()

    def connect_clicked(self):
        self.ui.l_conn.setText("Connecting to {}".format(self.uri))
        self.cf.connect(self.uri)

    def update_interface(self):
        ## labele od zmq
        # pozycje
        self.ui.l_x_2.setText("x: {:.3f}".format(self.x_cam))
        self.ui.l_y_2.setText("y: {:.3f}".format(self.y_cam))
        self.ui.l_z_2.setText("z: {:.3f}".format(self.z_cam))
        self.ui.l_theta_2.setText("yaw: {:.3f}".format(self.yaw_cam))

        # predkosci
        self.ui.l_vx_2.setText("thrust: {:.3f}".format(self.thrust_dron))
        self.ui.l_vy_2.setText("roll: {:.3f}".format(self.roll_dron))
        self.ui.l_vz_2.setText("pitch: {:.3f}".format(self.pitch_dron))
        self.ui.l_vtheta_2.setText("yaw: {:.3f}".format(self.yaw_dron))

        ## labele od cf
        self.ui.l_thrust_a_2.setText("Ez: {}".format(self.z_dron))
        self.ui.l_roll_a_2.setText("Ex: {}".format(self.x_dron))
        self.ui.l_pitch_a_2.setText("Ey: {}".format(self.y_dron))
        self.ui.l_yaw_a_2.setText("Eyaw: {}".format(self.alfa_dron))

        # labele od sterowania
        self.ui.l_thrust_2.setText("Thrust: {:}".format(self.thrust_control))
        self.ui.l_roll_2.setText("Roll: {:}".format(self.roll_control))
        self.ui.l_pitch_2.setText("Pitch: {:}".format(self.pitch_control))
        self.ui.l_yaw_2.setText("Yaw: {:}".format(self.yaw_control))


        #wypelnianie tabelek logow

    def update_log_table(self):
        self.ui.table_log.currentRow()
        currentRowCount = self.ui.table_log.rowCount() #necessary even when there are no rows in the table
        self.ui.table_log.insertRow(currentRowCount)

        self.ui.table_log.setItem(currentRowCount,0,QtGui.QTableWidgetItem("{}".format(time.strftime("%H:%M:%S"))))

        self.ui.table_log.setItem(currentRowCount,1,QtGui.QTableWidgetItem("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(
            self.x_cam,self.y_cam,self.z_cam,self.yaw_cam)))

        self.ui.table_log.setItem(currentRowCount,2,QtGui.QTableWidgetItem("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(
            self.x_target-self.x_cam,self.y_target-self.y_cam,self.z_target-self.z_cam,self.yaw_target-self.yaw_cam)))


        # self.ui.table_log.setItem(currentRowCount,3,QtGui.QTableWidgetItem("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(
        #     self.vx_actual,self.vy_actual,self.vz_actual,self.vyaw_actual)))

        self.ui.table_log.setItem(currentRowCount,5,QtGui.QTableWidgetItem("{}, {:.3f}, {:.3f}, {:.3f}".format(
            self.thrust_dron,self.roll_dron,self.pitch_dron,self.yaw_dron)))

        self.ui.table_log.setItem(currentRowCount,4,QtGui.QTableWidgetItem("{}, {:.3f}, {:.3f}, {:.3f}".format(
            self.thrust_control,self.roll_control,self.pitch_control,self.yaw_control)))

        self.ui.table_log.setItem(currentRowCount,6,QtGui.QTableWidgetItem("{:.3f}, {:.3f}, {:.3f}, {:.3f}".format(
            self.m1,self.m2,self.m3,self.m4)))


        self.ui.table_log.scrollToBottom()
        self.ui.table_log.resizeColumnsToContents()

    def start_clicked(self):
        if not self.ctrl_isTrue:
            self.ctrl_isTrue=True
            self.ui.pb_start_2.setText("stop")
            self.ui.pb_stop_2.setEnabled(True)
            self.update_clicked()
            self.update_control_thread.start(10)
        else:
            self.ctrl_isTrue=False
            self.ui.pb_start_2.setText("start")
            self.ui.pb_stop_2.setEnabled(True)
            self.stop_clicked()

    def stop_clicked(self):
        self.ui.pb_start_2.setEnabled(True)
        self.ui.pb_stop_2.setEnabled(False)
        self.control_package={
            "thrust":0.0,
            "pitch":0.0,
            "roll":0.0,
            "yaw":0.0,
        }
        self.control_data_sig.emit(self.control_package)
        self.update_control_thread.stop()

    def update_clicked(self):
        self.x_target=float(self.ui.en_x_2.text())
        self.y_target=float(self.ui.en_y_2.text())
        self.z_target=float(self.ui.en_z_2.text())
        self.yaw_target=float(self.ui.en_theta_2.text())

    def update_control(self):
        vzcam=0
        if (self.isCorrect==0.0) :
            self.thrust_control=self.thrust_control_previous
            self.roll_control=self.roll_control_previous
            self.pitch_control=self.pitch_control_previous
            self.yaw_control=self.yaw_control_previous
            self.timeout+=1
            print self.timeout
            if self.timeout>=15:
                self.control_package={
                    "thrust":0,
                    "pitch":0,
                    "roll":0,
                    "yaw":0
                }
                self.control_data_sig.emit(self.control_package)
                self.stop_clicked()
        else:
            # przypisanie sterowania do sterowania poprzedniego


            self.stan=self.kalman.licz(self.x_cam,self.y_cam,self.z_cam,self.roll_dron,self.pitch_dron,self.yaw_cam) #

            # self.vzcam=(self.z_cam-self.z_cam_p)/self.dt
            # self.z_cam_p=self.z_cam
            x=self.stan[0]
            y=self.stan[1]
            z=self.stan[2]
            roll=self.stan[3]
            pitch=self.stan[4]
            alfa=self.stan[5]
            vx=self.stan[6]
            vy=self.stan[7]
            vz=self.stan[8]
            vroll=self.stan[9]
            vpitch=self.stan[10]
            valfa=self.stan[11]

            self.x_dron=(self.x_target-x)*cos(alfa)+(self.y_target-y)*sin(alfa)
            self.y_dron=(self.y_target-y)*cos(alfa)-(self.x_target-x)*sin(alfa)
            self.z_dron=self.z_target-z
            self.vx_dron=vx*cos(alfa)+vy*sin(alfa)
            self.vy_dron=vy*cos(alfa)-vx*sin(alfa)
            self.vz_dron=vz
            self.alfa_dron=alfa
            self.valfa_dron=valfa




            # self.thrust_control=fz(self.z_dron,self.vz_dron)
            # self.roll_control=fd(self.y_dron,self.vy_dron)
            # self.pitch_control=fd(self.x_dron,self.vx_dron)
            # self.yaw_control=fyaw(alfa*180/pi,valfa*180/pi)
            # self.daneZ.e=self.z_dron
            T,Y,R,P=sprzezenie.control(self.z_dron,self.vz_dron,alfa,valfa,self.x_dron,self.vx_dron,self.y_dron,self.vy_dron,roll,pitch,vroll,vpitch)
            Tf=fz((self.z_dron)*100,self.vz_dron)
            Rf=-fd((self.y_dron),self.vy_dron)
            Pf=fd((self.x_dron),self.vx_dron)
            Yf=fyaw((self.yaw_target-alfa)*180/pi,valfa)

            self.thrust_control=Tf
            self.pitch_control=Pf
            self.roll_control=Rf
            self.yaw_control=Yf
            self.timeout=0


            # self.thrust_control=60
            # self.pitch_control=0.0
            # self.roll_control=0.0
            # self.yaw_control=30

            self.control_package={
                "thrust":self.thrust_control*600,
                "pitch":self.pitch_control,
                "roll":self.roll_control,
                "yaw":self.yaw_control
            }
            if self.ui.cb_sendCtrl.isChecked():
                self.control_data_sig.emit(self.control_package)


        # self.update_log_table()
        str1=",".join([str(self.x_cam),str(self.y_cam),str(self.z_cam),str(self.yaw_cam),str(self.vzcam)])
        str2=",".join(str(i) for i in self.stan)
        str3=",".join([str(self.pitch_control),str(self.roll_control),str(self.yaw_control),str(self.thrust_control)])
        str4=",".join([str(self.x_dron),str(self.y_dron),str(self.z_dron)])
        str5=",".join([str(self.roll_dron),str(self.pitch_dron),str(self.yaw_dron)])
        self.strlist.append(",".join([str1,str2,str3,str4,str5]))



        self.thrust_control_previous=self.thrust_control
        self.pitch_control_previous=self.pitch_control
        self.roll_control_previous=self.roll_control
        self.yaw_control_previous=self.yaw_control
        pass

    def stop_control_thread(self):
        self.stop_clicked()








