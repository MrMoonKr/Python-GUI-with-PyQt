# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label_eg1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 684)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 150, 701, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(340, 50, 20, 101))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.mylbl1 = QtWidgets.QLabel(self.centralwidget)
        self.mylbl1.setGeometry(QtCore.QRect(50, 80, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mylbl1.setFont(font)
        self.mylbl1.setObjectName("mylbl1")
        self.mylbl2 = QtWidgets.QLabel(self.centralwidget)
        self.mylbl2.setGeometry(QtCore.QRect(370, 80, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mylbl2.setFont(font)
        self.mylbl2.setObjectName("mylbl2")
        self.mylbl3 = QtWidgets.QLabel(self.centralwidget)
        self.mylbl3.setGeometry(QtCore.QRect(80, 210, 661, 391))
        self.mylbl3.setObjectName("mylbl3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(590, 80, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.mylbl1_2 = QtWidgets.QLabel(self.centralwidget)
        self.mylbl1_2.setGeometry(QtCore.QRect(300, 170, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mylbl1_2.setFont(font)
        self.mylbl1_2.setObjectName("mylbl1_2")
        self.mylbl1_3 = QtWidgets.QLabel(self.centralwidget)
        self.mylbl1_3.setGeometry(QtCore.QRect(310, 20, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mylbl1_3.setFont(font)
        self.mylbl1_3.setObjectName("mylbl1_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Label_eg1"))
        self.mylbl1.setText(_translate("MainWindow", " "))
        self.mylbl2.setText(_translate("MainWindow", " "))
        self.mylbl3.setText(_translate("MainWindow", " "))
        self.mylbl1_2.setText(_translate("MainWindow", "Horizontal Line"))
        self.mylbl1_3.setText(_translate("MainWindow", "Vertical Line"))
