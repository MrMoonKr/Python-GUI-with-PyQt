# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plaintextedit_eg1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 238)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 20, 301, 151))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.mybtn = QtWidgets.QPushButton(self.centralwidget)
        self.mybtn.setGeometry(QtCore.QRect(340, 40, 93, 28))
        self.mybtn.setObjectName("mybtn")
        self.mylbl = QtWidgets.QLabel(self.centralwidget)
        self.mylbl.setGeometry(QtCore.QRect(30, 180, 301, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mylbl.setFont(font)
        self.mylbl.setText("")
        self.mylbl.setObjectName("mylbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QPlainTextEdit_eg1"))
        self.mybtn.setText(_translate("MainWindow", "Add Text"))