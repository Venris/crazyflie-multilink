# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(578, 294)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.l_status = QtGui.QLabel(self.frame_3)
        self.l_status.setObjectName(_fromUtf8("l_status"))
        self.horizontalLayout_3.addWidget(self.l_status)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cb_device = QtGui.QComboBox(self.frame)
        self.cb_device.setObjectName(_fromUtf8("cb_device"))
        self.horizontalLayout.addWidget(self.cb_device)
        self.pb_scan = QtGui.QPushButton(self.frame)
        self.pb_scan.setObjectName(_fromUtf8("pb_scan"))
        self.horizontalLayout.addWidget(self.pb_scan)
        self.pb_conn = QtGui.QPushButton(self.frame)
        self.pb_conn.setObjectName(_fromUtf8("pb_conn"))
        self.horizontalLayout.addWidget(self.pb_conn)
        self.pb_disc = QtGui.QPushButton(self.frame)
        self.pb_disc.setObjectName(_fromUtf8("pb_disc"))
        self.horizontalLayout.addWidget(self.pb_disc)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.frame_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.l_gyro_x = QtGui.QLabel(self.groupBox)
        self.l_gyro_x.setObjectName(_fromUtf8("l_gyro_x"))
        self.verticalLayout.addWidget(self.l_gyro_x)
        self.l_gyro_y = QtGui.QLabel(self.groupBox)
        self.l_gyro_y.setObjectName(_fromUtf8("l_gyro_y"))
        self.verticalLayout.addWidget(self.l_gyro_y)
        self.l_gyro_z = QtGui.QLabel(self.groupBox)
        self.l_gyro_z.setObjectName(_fromUtf8("l_gyro_z"))
        self.verticalLayout.addWidget(self.l_gyro_z)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.l_acc_x = QtGui.QLabel(self.groupBox_2)
        self.l_acc_x.setObjectName(_fromUtf8("l_acc_x"))
        self.verticalLayout_2.addWidget(self.l_acc_x)
        self.l_acc_y = QtGui.QLabel(self.groupBox_2)
        self.l_acc_y.setObjectName(_fromUtf8("l_acc_y"))
        self.verticalLayout_2.addWidget(self.l_acc_y)
        self.l_acc_z = QtGui.QLabel(self.groupBox_2)
        self.l_acc_z.setObjectName(_fromUtf8("l_acc_z"))
        self.verticalLayout_2.addWidget(self.l_acc_z)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.l_roll = QtGui.QLabel(self.groupBox_3)
        self.l_roll.setObjectName(_fromUtf8("l_roll"))
        self.verticalLayout_3.addWidget(self.l_roll)
        self.l_pitch = QtGui.QLabel(self.groupBox_3)
        self.l_pitch.setObjectName(_fromUtf8("l_pitch"))
        self.verticalLayout_3.addWidget(self.l_pitch)
        self.l_yaw = QtGui.QLabel(self.groupBox_3)
        self.l_yaw.setObjectName(_fromUtf8("l_yaw"))
        self.verticalLayout_3.addWidget(self.l_yaw)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.l_pos_x = QtGui.QLabel(self.groupBox_4)
        self.l_pos_x.setObjectName(_fromUtf8("l_pos_x"))
        self.verticalLayout_4.addWidget(self.l_pos_x)
        self.l_pos_y = QtGui.QLabel(self.groupBox_4)
        self.l_pos_y.setObjectName(_fromUtf8("l_pos_y"))
        self.verticalLayout_4.addWidget(self.l_pos_y)
        self.l_pos_z = QtGui.QLabel(self.groupBox_4)
        self.l_pos_z.setObjectName(_fromUtf8("l_pos_z"))
        self.verticalLayout_4.addWidget(self.l_pos_z)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_5.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.l_status.setText(_translate("MainWindow", "Disconnected", None))
        self.pb_scan.setText(_translate("MainWindow", "Scan", None))
        self.pb_conn.setText(_translate("MainWindow", "Connect", None))
        self.pb_disc.setText(_translate("MainWindow", "Disconnect", None))
        self.groupBox.setTitle(_translate("MainWindow", "Gyro", None))
        self.l_gyro_x.setText(_translate("MainWindow", "x:", None))
        self.l_gyro_y.setText(_translate("MainWindow", "y:", None))
        self.l_gyro_z.setText(_translate("MainWindow", "z: ", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Acc", None))
        self.l_acc_x.setText(_translate("MainWindow", "x: ", None))
        self.l_acc_y.setText(_translate("MainWindow", "y: ", None))
        self.l_acc_z.setText(_translate("MainWindow", "z:", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "RPY", None))
        self.l_roll.setText(_translate("MainWindow", "Roll: ", None))
        self.l_pitch.setText(_translate("MainWindow", "Pitch: ", None))
        self.l_yaw.setText(_translate("MainWindow", "Yaw: ", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Position", None))
        self.l_pos_x.setText(_translate("MainWindow", "x:", None))
        self.l_pos_y.setText(_translate("MainWindow", "y: ", None))
        self.l_pos_z.setText(_translate("MainWindow", "z: ", None))

