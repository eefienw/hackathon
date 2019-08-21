# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\eclipse-workspace\autoconfigtool\Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(476, 356)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 288, 193, 28))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(11, 11, 341, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_addhost = QtWidgets.QLineEdit(dialog)
        self.lineEdit_addhost.setGeometry(QtCore.QRect(90, 59, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_addhost.setFont(font)
        self.lineEdit_addhost.setObjectName("lineEdit_addhost")
        self.label_hostname = QtWidgets.QLabel(dialog)
        self.label_hostname.setGeometry(QtCore.QRect(11, 60, 72, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_hostname.setFont(font)
        self.label_hostname.setObjectName("label_hostname")
        self.lineEdit_addIP = QtWidgets.QLineEdit(dialog)
        self.lineEdit_addIP.setGeometry(QtCore.QRect(90, 123, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_addIP.setFont(font)
        self.lineEdit_addIP.setObjectName("lineEdit_addIP")
        self.label_IP = QtWidgets.QLabel(dialog)
        self.label_IP.setGeometry(QtCore.QRect(11, 126, 72, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_IP.setFont(font)
        self.label_IP.setObjectName("label_IP")
        self.lineEdit_addMAC = QtWidgets.QLineEdit(dialog)
        self.lineEdit_addMAC.setGeometry(QtCore.QRect(90, 186, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_addMAC.setFont(font)
        self.lineEdit_addMAC.setObjectName("lineEdit_addMAC")
        self.label_MAC = QtWidgets.QLabel(dialog)
        self.label_MAC.setGeometry(QtCore.QRect(11, 188, 72, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_MAC.setFont(font)
        self.label_MAC.setObjectName("label_MAC")

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.label.setText(_translate("dialog", "Please input the hostname ip and mac info"))
        self.label_hostname.setText(_translate("dialog", "Hostname:"))
        self.label_IP.setText(_translate("dialog", "IP :"))
        self.label_MAC.setText(_translate("dialog", "MAC :"))
