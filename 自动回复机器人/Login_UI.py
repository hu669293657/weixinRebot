# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(560, 380)
        MainWindow.setFixedSize(560, 380)

        MainWindow.setWindowIcon(QIcon('logo.png'))
        MainWindow.setStyleSheet("background-image:url(robot.png)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 200, 150, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 240, 150, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(170, 200, 50, 20))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setGeometry(QtCore.QRect(180, 245, 50, 20))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 280, 100, 23))
        self.pushButton.setObjectName("pushButton")
        self.login_button = QtWidgets.QPushButton(self.centralWidget)
        self.login_button.setGeometry(QtCore.QRect(340, 280, 100, 23))
        self.login_button.setObjectName("login_button")
        MainWindow.setCentralWidget(self.centralWidget)

        # 设置控件的属性,UI界面和功能分离

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "AI智能回复机器人"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入电话号码"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入六位密码"))
        self.label.setText(_translate("MainWindow", "帐号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "注册"))
        self.login_button.setText(_translate("MainWindow", "登录"))