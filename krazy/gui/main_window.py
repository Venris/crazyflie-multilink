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
        MainWindow.resize(634, 496)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cb_devices = QtGui.QComboBox(self.frame)
        self.cb_devices.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_devices.setObjectName(_fromUtf8("cb_devices"))
        self.horizontalLayout.addWidget(self.cb_devices)
        self.pb_scan_devices = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_scan_devices.sizePolicy().hasHeightForWidth())
        self.pb_scan_devices.setSizePolicy(sizePolicy)
        self.pb_scan_devices.setFlat(False)
        self.pb_scan_devices.setObjectName(_fromUtf8("pb_scan_devices"))
        self.horizontalLayout.addWidget(self.pb_scan_devices)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.en_id = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.en_id.sizePolicy().hasHeightForWidth())
        self.en_id.setSizePolicy(sizePolicy)
        self.en_id.setObjectName(_fromUtf8("en_id"))
        self.horizontalLayout.addWidget(self.en_id)
        self.pb_add_dron = QtGui.QPushButton(self.frame)
        self.pb_add_dron.setObjectName(_fromUtf8("pb_add_dron"))
        self.horizontalLayout.addWidget(self.pb_add_dron)
        self.pb_remove = QtGui.QPushButton(self.frame)
        self.pb_remove.setObjectName(_fromUtf8("pb_remove"))
        self.horizontalLayout.addWidget(self.pb_remove)
        self.verticalLayout.addWidget(self.frame)
        self.layout_drons = QtGui.QGridLayout()
        self.layout_drons.setObjectName(_fromUtf8("layout_drons"))
        self.verticalLayout.addLayout(self.layout_drons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pb_scan_devices.setText(_translate("MainWindow", "Scan", None))
        self.en_id.setText(_translate("MainWindow", "0", None))
        self.pb_add_dron.setText(_translate("MainWindow", "Add", None))
        self.pb_remove.setText(_translate("MainWindow", "Remove all", None))

