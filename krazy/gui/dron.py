# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dron.ui'
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

class Ui_Dron(object):
    def setupUi(self, Dron):
        Dron.setObjectName(_fromUtf8("Dron"))
        Dron.resize(755, 373)
        self.verticalLayout = QtGui.QVBoxLayout(Dron)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dron)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gb_connection = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_connection.sizePolicy().hasHeightForWidth())
        self.gb_connection.setSizePolicy(sizePolicy)
        self.gb_connection.setObjectName(_fromUtf8("gb_connection"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.gb_connection)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.l_conn = QtGui.QLabel(self.gb_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_conn.sizePolicy().hasHeightForWidth())
        self.l_conn.setSizePolicy(sizePolicy)
        self.l_conn.setObjectName(_fromUtf8("l_conn"))
        self.horizontalLayout_4.addWidget(self.l_conn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pb_conn_2 = QtGui.QPushButton(self.gb_connection)
        self.pb_conn_2.setEnabled(True)
        self.pb_conn_2.setObjectName(_fromUtf8("pb_conn_2"))
        self.horizontalLayout_4.addWidget(self.pb_conn_2)
        self.pb_disc_2 = QtGui.QPushButton(self.gb_connection)
        self.pb_disc_2.setEnabled(False)
        self.pb_disc_2.setObjectName(_fromUtf8("pb_disc_2"))
        self.horizontalLayout_4.addWidget(self.pb_disc_2)
        self.gridLayout.addWidget(self.gb_connection, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gb_actual_2 = QtGui.QGroupBox(self.frame_2)
        self.gb_actual_2.setMinimumSize(QtCore.QSize(80, 0))
        self.gb_actual_2.setObjectName(_fromUtf8("gb_actual_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.gb_actual_2)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.l_z_2 = QtGui.QLabel(self.gb_actual_2)
        self.l_z_2.setObjectName(_fromUtf8("l_z_2"))
        self.verticalLayout_8.addWidget(self.l_z_2)
        self.l_x_2 = QtGui.QLabel(self.gb_actual_2)
        self.l_x_2.setObjectName(_fromUtf8("l_x_2"))
        self.verticalLayout_8.addWidget(self.l_x_2)
        self.l_y_2 = QtGui.QLabel(self.gb_actual_2)
        self.l_y_2.setObjectName(_fromUtf8("l_y_2"))
        self.verticalLayout_8.addWidget(self.l_y_2)
        self.l_theta_2 = QtGui.QLabel(self.gb_actual_2)
        self.l_theta_2.setObjectName(_fromUtf8("l_theta_2"))
        self.verticalLayout_8.addWidget(self.l_theta_2)
        self.horizontalLayout_3.addWidget(self.gb_actual_2)
        self.groupBox_3 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(80, 0))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.l_vz_2 = QtGui.QLabel(self.groupBox_3)
        self.l_vz_2.setObjectName(_fromUtf8("l_vz_2"))
        self.verticalLayout_9.addWidget(self.l_vz_2)
        self.l_vx_2 = QtGui.QLabel(self.groupBox_3)
        self.l_vx_2.setObjectName(_fromUtf8("l_vx_2"))
        self.verticalLayout_9.addWidget(self.l_vx_2)
        self.l_vy_2 = QtGui.QLabel(self.groupBox_3)
        self.l_vy_2.setObjectName(_fromUtf8("l_vy_2"))
        self.verticalLayout_9.addWidget(self.l_vy_2)
        self.l_vtheta_2 = QtGui.QLabel(self.groupBox_3)
        self.l_vtheta_2.setObjectName(_fromUtf8("l_vtheta_2"))
        self.verticalLayout_9.addWidget(self.l_vtheta_2)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.gb_target_2 = QtGui.QGroupBox(self.frame_2)
        self.gb_target_2.setEnabled(True)
        self.gb_target_2.setObjectName(_fromUtf8("gb_target_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.gb_target_2)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.en_z_2 = QtGui.QLineEdit(self.gb_target_2)
        self.en_z_2.setObjectName(_fromUtf8("en_z_2"))
        self.verticalLayout_10.addWidget(self.en_z_2)
        self.en_x_2 = QtGui.QLineEdit(self.gb_target_2)
        self.en_x_2.setObjectName(_fromUtf8("en_x_2"))
        self.verticalLayout_10.addWidget(self.en_x_2)
        self.en_y_2 = QtGui.QLineEdit(self.gb_target_2)
        self.en_y_2.setObjectName(_fromUtf8("en_y_2"))
        self.verticalLayout_10.addWidget(self.en_y_2)
        self.en_theta_2 = QtGui.QLineEdit(self.gb_target_2)
        self.en_theta_2.setObjectName(_fromUtf8("en_theta_2"))
        self.verticalLayout_10.addWidget(self.en_theta_2)
        self.horizontalLayout_3.addWidget(self.gb_target_2)
        self.groupBox_4 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.l_thrust_a_2 = QtGui.QLabel(self.groupBox_4)
        self.l_thrust_a_2.setObjectName(_fromUtf8("l_thrust_a_2"))
        self.verticalLayout_11.addWidget(self.l_thrust_a_2)
        self.l_roll_a_2 = QtGui.QLabel(self.groupBox_4)
        self.l_roll_a_2.setObjectName(_fromUtf8("l_roll_a_2"))
        self.verticalLayout_11.addWidget(self.l_roll_a_2)
        self.l_pitch_a_2 = QtGui.QLabel(self.groupBox_4)
        self.l_pitch_a_2.setObjectName(_fromUtf8("l_pitch_a_2"))
        self.verticalLayout_11.addWidget(self.l_pitch_a_2)
        self.l_yaw_a_2 = QtGui.QLabel(self.groupBox_4)
        self.l_yaw_a_2.setObjectName(_fromUtf8("l_yaw_a_2"))
        self.verticalLayout_11.addWidget(self.l_yaw_a_2)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.gb_ctrl_data_2 = QtGui.QGroupBox(self.frame_2)
        self.gb_ctrl_data_2.setMinimumSize(QtCore.QSize(100, 0))
        self.gb_ctrl_data_2.setObjectName(_fromUtf8("gb_ctrl_data_2"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.gb_ctrl_data_2)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.l_thrust_2 = QtGui.QLabel(self.gb_ctrl_data_2)
        self.l_thrust_2.setObjectName(_fromUtf8("l_thrust_2"))
        self.verticalLayout_12.addWidget(self.l_thrust_2)
        self.l_roll_2 = QtGui.QLabel(self.gb_ctrl_data_2)
        self.l_roll_2.setObjectName(_fromUtf8("l_roll_2"))
        self.verticalLayout_12.addWidget(self.l_roll_2)
        self.l_pitch_2 = QtGui.QLabel(self.gb_ctrl_data_2)
        self.l_pitch_2.setObjectName(_fromUtf8("l_pitch_2"))
        self.verticalLayout_12.addWidget(self.l_pitch_2)
        self.l_yaw_2 = QtGui.QLabel(self.gb_ctrl_data_2)
        self.l_yaw_2.setObjectName(_fromUtf8("l_yaw_2"))
        self.verticalLayout_12.addWidget(self.l_yaw_2)
        self.horizontalLayout_3.addWidget(self.gb_ctrl_data_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gb_control_2 = QtGui.QGroupBox(self.frame_2)
        self.gb_control_2.setEnabled(False)
        self.gb_control_2.setObjectName(_fromUtf8("gb_control_2"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.gb_control_2)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.cb_sendCtrl = QtGui.QCheckBox(self.gb_control_2)
        self.cb_sendCtrl.setChecked(False)
        self.cb_sendCtrl.setObjectName(_fromUtf8("cb_sendCtrl"))
        self.verticalLayout_13.addWidget(self.cb_sendCtrl)
        self.pb_start_2 = QtGui.QPushButton(self.gb_control_2)
        self.pb_start_2.setEnabled(False)
        self.pb_start_2.setObjectName(_fromUtf8("pb_start_2"))
        self.verticalLayout_13.addWidget(self.pb_start_2)
        self.pb_update_2 = QtGui.QPushButton(self.gb_control_2)
        self.pb_update_2.setEnabled(False)
        self.pb_update_2.setObjectName(_fromUtf8("pb_update_2"))
        self.verticalLayout_13.addWidget(self.pb_update_2)
        self.pb_stop_2 = QtGui.QPushButton(self.gb_control_2)
        self.pb_stop_2.setEnabled(False)
        self.pb_stop_2.setObjectName(_fromUtf8("pb_stop_2"))
        self.verticalLayout_13.addWidget(self.pb_stop_2)
        self.pb_save = QtGui.QPushButton(self.gb_control_2)
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.verticalLayout_13.addWidget(self.pb_save)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.gb_control_2)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.table_log = QtGui.QTableWidget(self.tab_2)
        self.table_log.setObjectName(_fromUtf8("table_log"))
        self.table_log.setColumnCount(7)
        self.table_log.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(6, item)
        self.gridLayout_2.addWidget(self.table_log, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dron)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dron)

    def retranslateUi(self, Dron):
        Dron.setWindowTitle(_translate("Dron", "Dron", None))
        self.gb_connection.setTitle(_translate("Dron", "Connection", None))
        self.l_conn.setText(_translate("Dron", "Disconnected", None))
        self.pb_conn_2.setText(_translate("Dron", "Connect", None))
        self.pb_disc_2.setText(_translate("Dron", "Disconnect", None))
        self.gb_actual_2.setTitle(_translate("Dron", "Actual", None))
        self.l_z_2.setText(_translate("Dron", "Z: ", None))
        self.l_x_2.setText(_translate("Dron", "X: ", None))
        self.l_y_2.setText(_translate("Dron", "Y: ", None))
        self.l_theta_2.setText(_translate("Dron", "Kat: ", None))
        self.groupBox_3.setTitle(_translate("Dron", "Actual V", None))
        self.l_vz_2.setText(_translate("Dron", "Vz", None))
        self.l_vx_2.setText(_translate("Dron", "Vx: ", None))
        self.l_vy_2.setText(_translate("Dron", "Vy: ", None))
        self.l_vtheta_2.setText(_translate("Dron", "Vkat", None))
        self.gb_target_2.setTitle(_translate("Dron", "Target x,y,z,kat", None))
        self.en_z_2.setText(_translate("Dron", "0.4", None))
        self.en_x_2.setText(_translate("Dron", "0", None))
        self.en_y_2.setText(_translate("Dron", "0", None))
        self.en_theta_2.setText(_translate("Dron", "0", None))
        self.groupBox_4.setTitle(_translate("Dron", "Actual TRPY", None))
        self.l_thrust_a_2.setText(_translate("Dron", "Thrust:", None))
        self.l_roll_a_2.setText(_translate("Dron", "Roll:", None))
        self.l_pitch_a_2.setText(_translate("Dron", "Pitch", None))
        self.l_yaw_a_2.setText(_translate("Dron", "Yaw:", None))
        self.gb_ctrl_data_2.setTitle(_translate("Dron", "Control data", None))
        self.l_thrust_2.setText(_translate("Dron", "Thrust: ", None))
        self.l_roll_2.setText(_translate("Dron", "Roll:", None))
        self.l_pitch_2.setText(_translate("Dron", "Pitch:", None))
        self.l_yaw_2.setText(_translate("Dron", "Yaw:", None))
        self.gb_control_2.setTitle(_translate("Dron", "Control", None))
        self.cb_sendCtrl.setText(_translate("Dron", "send ctrl", None))
        self.pb_start_2.setText(_translate("Dron", "Start", None))
        self.pb_update_2.setText(_translate("Dron", "Update", None))
        self.pb_stop_2.setText(_translate("Dron", "Stop", None))
        self.pb_save.setText(_translate("Dron", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dron", "Tab 1", None))
        item = self.table_log.horizontalHeaderItem(0)
        item.setText(_translate("Dron", "Time", None))
        item = self.table_log.horizontalHeaderItem(1)
        item.setText(_translate("Dron", "X,Y,Z,Yaw -cam", None))
        item = self.table_log.horizontalHeaderItem(2)
        item.setText(_translate("Dron", "X,Y,Z,Yaw -errors", None))
        item = self.table_log.horizontalHeaderItem(3)
        item.setText(_translate("Dron", "X,Y,Z,Yaw - V", None))
        item = self.table_log.horizontalHeaderItem(4)
        item.setText(_translate("Dron", "TRPY-control", None))
        item = self.table_log.horizontalHeaderItem(5)
        item.setText(_translate("Dron", "TRPY - dron", None))
        item = self.table_log.horizontalHeaderItem(6)
        item.setText(_translate("Dron", "motors", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dron", "Tab 2", None))

