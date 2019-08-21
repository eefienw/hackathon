# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atuoconfig.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QLineEdit, QInputDialog,QMessageBox,QDialog
#from autoconfig import dialogUI, dhcpcfg
#import dialogUI, dhcpcfg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.configpage = QtWidgets.QTabWidget(self.centralwidget)
        self.configpage.setGeometry(QtCore.QRect(50, 30, 1031, 761))
        
        self.configpage.setObjectName("configpage")
        self.stpconfig = QtWidgets.QWidget()
        self.stpconfig.setObjectName("stpconfig")
        
        self.pushButton_ok = QtWidgets.QPushButton(self.stpconfig)
        self.pushButton_ok.setGeometry(QtCore.QRect(780, 690, 71, 21))
        self.pushButton_ok.setObjectName("pushButton_ok")
        
        self.pushButton_cancel = QtWidgets.QPushButton(self.stpconfig)
        self.pushButton_cancel.setGeometry(QtCore.QRect(890, 688, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        
        self.groupBox_checkpoint = QtWidgets.QGroupBox(self.stpconfig)
        self.groupBox_checkpoint.setGeometry(QtCore.QRect(13, 158, 401, 211))
        self.groupBox_checkpoint.setObjectName("groupBox_checkpoint")
        
        self.checkBox_network = QtWidgets.QCheckBox(self.groupBox_checkpoint)
        self.checkBox_network.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.checkBox_network.setObjectName("checkBox_network")
        
        self.checkBox_tsport = QtWidgets.QCheckBox(self.groupBox_checkpoint)
        self.checkBox_tsport.setGeometry(QtCore.QRect(20, 70, 91, 20))
        self.checkBox_tsport.setObjectName("checkBox_tsport")
        
        self.checkBox_cpri = QtWidgets.QCheckBox(self.groupBox_checkpoint)
        self.checkBox_cpri.setGeometry(QtCore.QRect(20, 110, 81, 20))
        self.checkBox_cpri.setObjectName("checkBox_cpri")
        
        self.checkBox_iqdata = QtWidgets.QCheckBox(self.groupBox_checkpoint)
        self.checkBox_iqdata.setGeometry(QtCore.QRect(20, 150, 81, 20))
        self.checkBox_iqdata.setObjectName("checkBox_iqdata")
        
        self.label_netstatus = QtWidgets.QLabel(self.groupBox_checkpoint)
        self.label_netstatus.setGeometry(QtCore.QRect(130, 33, 81, 16))
        self.label_netstatus.setObjectName("label_netstatus")
        
        self.label_tpstatus = QtWidgets.QLabel(self.groupBox_checkpoint)
        self.label_tpstatus.setGeometry(QtCore.QRect(130, 72, 81, 16))
        self.label_tpstatus.setObjectName("label_tpstatus")
        
        self.label_cpristatus = QtWidgets.QLabel(self.groupBox_checkpoint)
        self.label_cpristatus.setGeometry(QtCore.QRect(131, 110, 81, 16))
        self.label_cpristatus.setObjectName("label_cpristatus")
        
        self.label_iqstatus = QtWidgets.QLabel(self.groupBox_checkpoint)
        self.label_iqstatus.setGeometry(QtCore.QRect(130, 151, 81, 16))
        self.label_iqstatus.setObjectName("label_iqstatus")
        
        self.pushButton_check = QtWidgets.QPushButton(self.groupBox_checkpoint)
        self.pushButton_check.setGeometry(QtCore.QRect(300, 170, 75, 23))
        self.pushButton_check.setObjectName("pushButton_check")
        
        self.groupBox_configpoint = QtWidgets.QGroupBox(self.stpconfig)
        self.groupBox_configpoint.setGeometry(QtCore.QRect(13, 388, 1021, 281))
        self.groupBox_configpoint.setObjectName("groupBox_configpoint")
        self.groupBox_cfgnetwork = QtWidgets.QGroupBox(self.groupBox_configpoint)
        self.groupBox_cfgnetwork.setGeometry(QtCore.QRect(20, 29, 961, 61))
        self.groupBox_cfgnetwork.setObjectName("groupBox_cfgnetwork")
        
        self.label_configip = QtWidgets.QLabel(self.groupBox_cfgnetwork)
        self.label_configip.setGeometry(QtCore.QRect(11, 26, 55, 16))
        self.label_configip.setObjectName("label_configip")
        
        self.lineEdit_configip = QtWidgets.QLineEdit(self.groupBox_cfgnetwork)
        self.lineEdit_configip.setGeometry(QtCore.QRect(60, 23, 111, 22))
        self.lineEdit_configip.setText("")
        self.lineEdit_configip.setObjectName("lineEdit_configip")
        self.lineEdit_gateway = QtWidgets.QLineEdit(self.groupBox_cfgnetwork)
        self.lineEdit_gateway.setGeometry(QtCore.QRect(309, 23, 121, 22))
       
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        
        self.lineEdit_gateway.setFont(font)
        self.lineEdit_gateway.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_gateway.setText("")
        self.lineEdit_gateway.setObjectName("lineEdit_gateway")
       
        self.label_gateway = QtWidgets.QLabel(self.groupBox_cfgnetwork)
        self.label_gateway.setGeometry(QtCore.QRect(239, 26, 61, 16))
        self.label_gateway.setObjectName("label_gateway")
        
        self.pushButton_cfgnetsub = QtWidgets.QPushButton(self.groupBox_cfgnetwork)
        self.pushButton_cfgnetsub.setGeometry(QtCore.QRect(836, 20, 81, 28))
        self.pushButton_cfgnetsub.setObjectName("pushButton_cfgnetsub")
        
        self.label_DNS = QtWidgets.QLabel(self.groupBox_cfgnetwork)
        self.label_DNS.setGeometry(QtCore.QRect(518, 27, 55, 16))
        self.label_DNS.setObjectName("label_DNS")
        
        self.lineEdit_DNS = QtWidgets.QLineEdit(self.groupBox_cfgnetwork)
        self.lineEdit_DNS.setGeometry(QtCore.QRect(556, 24, 131, 22))
        self.lineEdit_DNS.setText("")
        self.lineEdit_DNS.setObjectName("lineEdit_DNS")
        
        self.groupBox_cfgterminal = QtWidgets.QGroupBox(self.groupBox_configpoint)
        self.groupBox_cfgterminal.setGeometry(QtCore.QRect(20, 112, 961, 61))
        self.groupBox_cfgterminal.setObjectName("groupBox_cfgterminal")
        
        self.label_tspos = QtWidgets.QLabel(self.groupBox_cfgterminal)
        self.label_tspos.setGeometry(QtCore.QRect(10, 24, 55, 16))
        self.label_tspos.setObjectName("label_tspos")
        
        self.lineEdit_tspos = QtWidgets.QLineEdit(self.groupBox_cfgterminal)
        self.lineEdit_tspos.setGeometry(QtCore.QRect(60, 22, 111, 22))
        self.lineEdit_tspos.setObjectName("lineEdit_tspos")
        
        self.label_tsip = QtWidgets.QLabel(self.groupBox_cfgterminal)
        self.label_tsip.setGeometry(QtCore.QRect(239, 25, 55, 16))
        self.label_tsip.setObjectName("label_tsip")
        
        self.lineEdit_tsip = QtWidgets.QLineEdit(self.groupBox_cfgterminal)
        self.lineEdit_tsip.setGeometry(QtCore.QRect(308, 24, 121, 22))
        self.lineEdit_tsip.setObjectName("lineEdit_tsip")
        
        self.label_tsports = QtWidgets.QLabel(self.groupBox_cfgterminal)
        self.label_tsports.setGeometry(QtCore.QRect(518, 22, 61, 16))
        self.label_tsports.setObjectName("label_tsports")
        
        self.pushButton_cfgtssub = QtWidgets.QPushButton(self.groupBox_cfgterminal)
        self.pushButton_cfgtssub.setGeometry(QtCore.QRect(836, 19, 81, 28))
        self.pushButton_cfgtssub.setObjectName("pushButton_cfgtssub")
        
        self.comboBox_tsports = QtWidgets.QComboBox(self.groupBox_cfgterminal)
        self.comboBox_tsports.setGeometry(QtCore.QRect(605, 22, 73, 22))
        self.comboBox_tsports.setObjectName("comboBox_tsports")
        
        self.groupBox_cfgruma = QtWidgets.QGroupBox(self.groupBox_configpoint)
        self.groupBox_cfgruma.setGeometry(QtCore.QRect(20, 190, 961, 61))
        self.groupBox_cfgruma.setObjectName("groupBox_cfgruma")
        
        self.label_rumapos = QtWidgets.QLabel(self.groupBox_cfgruma)
        self.label_rumapos.setGeometry(QtCore.QRect(11, 26, 55, 16))
        self.label_rumapos.setObjectName("label_rumapos")
        
        self.lineEdit_rumapos = QtWidgets.QLineEdit(self.groupBox_cfgruma)
        self.lineEdit_rumapos.setGeometry(QtCore.QRect(64, 24, 101, 22))
        self.lineEdit_rumapos.setObjectName("lineEdit_rumapos")
        
        self.lineEdit_rumaip = QtWidgets.QLineEdit(self.groupBox_cfgruma)
        self.lineEdit_rumaip.setGeometry(QtCore.QRect(310, 21, 121, 22))
        self.lineEdit_rumaip.setObjectName("lineEdit_rumaip")
        
        self.label_rumaip = QtWidgets.QLabel(self.groupBox_cfgruma)
        self.label_rumaip.setGeometry(QtCore.QRect(236, 26, 61, 16))
        self.label_rumaip.setObjectName("label_rumaip")
        
        self.label_rumaports = QtWidgets.QLabel(self.groupBox_cfgruma)
        self.label_rumaports.setGeometry(QtCore.QRect(519, 24, 81, 16))
        self.label_rumaports.setObjectName("label_rumaports")
        
        self.pushButton_cfgrumasub = QtWidgets.QPushButton(self.groupBox_cfgruma)
        self.pushButton_cfgrumasub.setGeometry(QtCore.QRect(839, 18, 81, 28))
        self.pushButton_cfgrumasub.setObjectName("pushButton_cfgrumasub")
        
        self.comboBox_rumaports = QtWidgets.QComboBox(self.groupBox_cfgruma)
        self.comboBox_rumaports.setGeometry(QtCore.QRect(610, 21, 73, 22))
        self.comboBox_rumaports.setObjectName("comboBox_rumaports")
        
        self.groupBox_log = QtWidgets.QGroupBox(self.stpconfig)
        self.groupBox_log.setGeometry(QtCore.QRect(460, 160, 521, 211))
        self.groupBox_log.setObjectName("groupBox_log")
        
        self.connection = QtWidgets.QGroupBox(self.stpconfig)
        self.connection.setGeometry(QtCore.QRect(20, 10, 971, 141))
        self.connection.setObjectName("connection")
        
        self.label_user = QtWidgets.QLabel(self.connection)
        self.label_user.setGeometry(QtCore.QRect(248, 21, 47, 21))
        self.label_user.setTextFormat(QtCore.Qt.RichText)
        self.label_user.setObjectName("label_user")
        
        self.label_serverip = QtWidgets.QLabel(self.connection)
        self.label_serverip.setGeometry(QtCore.QRect(18, 17, 81, 31))
        self.label_serverip.setTextFormat(QtCore.Qt.RichText)
        self.label_serverip.setScaledContents(False)
        self.label_serverip.setWordWrap(False)
        self.label_serverip.setObjectName("label_serverip")
        
        self.lineEdit_passwd = QtWidgets.QLineEdit(self.connection)
        self.lineEdit_passwd.setGeometry(QtCore.QRect(538, 22, 131, 21))
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        
        self.lineEdit_serverip = QtWidgets.QLineEdit(self.connection)
        self.lineEdit_serverip.setGeometry(QtCore.QRect(98, 22, 131, 21))
        self.lineEdit_serverip.setObjectName("lineEdit_serverip")
        
        self.lineEdit_port = QtWidgets.QLineEdit(self.connection)
        self.lineEdit_port.setGeometry(QtCore.QRect(738, 22, 91, 21))
        self.lineEdit_port.setObjectName("lineEdit_port")
        
        self.lineEdit_user = QtWidgets.QLineEdit(self.connection)
        self.lineEdit_user.setGeometry(QtCore.QRect(291, 21, 131, 21))
        self.lineEdit_user.setObjectName("lineEdit_user")
        
        self.label_port = QtWidgets.QLabel(self.connection)
        self.label_port.setGeometry(QtCore.QRect(698, 20, 41, 21))
        self.label_port.setObjectName("label_port")
        
        self.pushButton_stpconnection = QtWidgets.QPushButton(self.connection)
        self.pushButton_stpconnection.setGeometry(QtCore.QRect(740, 90, 91, 31))
        self.pushButton_stpconnection.setObjectName("pushButton_stpconnection")
        
        self.groupBox_session = QtWidgets.QGroupBox(self.connection)
        self.groupBox_session.setGeometry(QtCore.QRect(10, 60, 411, 71))
        self.groupBox_session.setObjectName("groupBox_session")
        
        self.radioButton_ssh = QtWidgets.QRadioButton(self.groupBox_session)
        self.radioButton_ssh.setGeometry(QtCore.QRect(40, 34, 82, 17))
        self.radioButton_ssh.setObjectName("radioButton_ssh")
        
        self.radioButton_telnet = QtWidgets.QRadioButton(self.groupBox_session)
        self.radioButton_telnet.setGeometry(QtCore.QRect(158, 34, 82, 17))
        self.radioButton_telnet.setObjectName("radioButton_telnet")
        
        self.radioButton_ct11 = QtWidgets.QRadioButton(self.groupBox_session)
        self.radioButton_ct11.setGeometry(QtCore.QRect(276, 34, 71, 17))
        self.radioButton_ct11.setObjectName("radioButton_ct11")
        
        self.label_passwd = QtWidgets.QLabel(self.connection)
        self.label_passwd.setGeometry(QtCore.QRect(468, 21, 71, 21))
        self.label_passwd.setObjectName("label_passwd")
        
        self.textEdit_log = QtWidgets.QTextEdit(self.stpconfig)
        self.textEdit_log.setGeometry(QtCore.QRect(480, 177, 481, 181))
        self.textEdit_log.setObjectName("textEdit_log")
        
        self.configpage.addTab(self.stpconfig, "")
        self.dhcpcofig = QtWidgets.QWidget()
        self.dhcpcofig.setObjectName("dhcpcofig")
        
        self.groupBox_dhcpconfig = QtWidgets.QGroupBox(self.dhcpcofig)
        self.groupBox_dhcpconfig.setGeometry(QtCore.QRect(20, 150, 431, 531))
        self.groupBox_dhcpconfig.setObjectName("groupBox_dhcpconfig")
        
        self.groupBox_add = QtWidgets.QGroupBox(self.groupBox_dhcpconfig)
        self.groupBox_add.setGeometry(QtCore.QRect(20, 40, 341, 181))
        self.groupBox_add.setObjectName("groupBox_add")
        
        self.lineEdit_addip = QtWidgets.QLineEdit(self.groupBox_add)
        self.lineEdit_addip.setGeometry(QtCore.QRect(88, 84, 181, 22))
        self.lineEdit_addip.setObjectName("lineEdit_addip")
        
        
        self.label_addip = QtWidgets.QLabel(self.groupBox_add)
        self.label_addip.setGeometry(QtCore.QRect(11, 85, 55, 16))
        self.label_addip.setObjectName("label_addip")
        
        self.label_addmac = QtWidgets.QLabel(self.groupBox_add)
        self.label_addmac.setGeometry(QtCore.QRect(10, 131, 55, 16))
        self.label_addmac.setObjectName("label_addmac")
        
        self.lineEdit_addmac = QtWidgets.QLineEdit(self.groupBox_add)
        self.lineEdit_addmac.setGeometry(QtCore.QRect(88, 131, 181, 22))
        self.lineEdit_addmac.setText("")
        self.lineEdit_addmac.setObjectName("lineEdit_addmac")
        
        self.label_addhostname = QtWidgets.QLabel(self.groupBox_add)
        self.label_addhostname.setGeometry(QtCore.QRect(11, 42, 55, 16))
        self.label_addhostname.setObjectName("label_addhostname")
        
        self.lineEdit_addhostname = QtWidgets.QLineEdit(self.groupBox_add)
        self.lineEdit_addhostname.setGeometry(QtCore.QRect(88, 40, 181, 22))
        self.lineEdit_addhostname.setObjectName("lineEdit_addhostname")
        
        self.pushButton_cfgok = QtWidgets.QPushButton(self.groupBox_dhcpconfig)
        self.pushButton_cfgok.setGeometry(QtCore.QRect(210, 470, 93, 28))
        self.pushButton_cfgok.setObjectName("pushButton_cfgok")
        
        self.pushButton_cfgcancel = QtWidgets.QPushButton(self.groupBox_dhcpconfig)
        self.pushButton_cfgcancel.setGeometry(QtCore.QRect(320, 470, 93, 28))
        self.pushButton_cfgcancel.setObjectName("pushButton_cfgcancel")
        
        self.groupBox_configchoice = QtWidgets.QGroupBox(self.groupBox_dhcpconfig)
        self.groupBox_configchoice.setGeometry(QtCore.QRect(20, 230, 341, 221))
        self.groupBox_configchoice.setObjectName("groupBox_configchoice")
        
        self.radioButton_search = QtWidgets.QRadioButton(self.groupBox_configchoice)
        self.radioButton_search.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.radioButton_search.setObjectName("radioButton_search")
        
        self.radioButton_del = QtWidgets.QRadioButton(self.groupBox_configchoice)
        self.radioButton_del.setGeometry(QtCore.QRect(10, 110, 95, 20))
        self.radioButton_del.setObjectName("radioButton_del")
        
        
        self.radioButton_add = QtWidgets.QRadioButton(self.groupBox_configchoice)
        self.radioButton_add.setGeometry(QtCore.QRect(10, 70, 95, 20))
        self.radioButton_add.setObjectName("radioButton_add")
        
        
        self.radioButton_modify = QtWidgets.QRadioButton(self.groupBox_configchoice)
        self.radioButton_modify.setGeometry(QtCore.QRect(10, 150, 95, 20))
        self.radioButton_modify.setObjectName("radioButton_modify")
        
        self.radioButton_backup = QtWidgets.QRadioButton(self.groupBox_configchoice)
        self.radioButton_backup.setGeometry(QtCore.QRect(10, 190, 95, 20))
        self.radioButton_backup.setObjectName("radioButton_backup")
       
        self.groupBox_connect = QtWidgets.QGroupBox(self.dhcpcofig)
        self.groupBox_connect.setGeometry(QtCore.QRect(0, 20, 991, 121))
        self.groupBox_connect.setObjectName("groupBox_connect")
        
        self.label_dhcpip = QtWidgets.QLabel(self.groupBox_connect)
        self.label_dhcpip.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.label_dhcpip.setObjectName("label_dhcpip")
        
        self.lineEdit_dhcpip = QtWidgets.QLineEdit(self.groupBox_connect)
        self.lineEdit_dhcpip.setGeometry(QtCore.QRect(101, 45, 151, 22))
        self.lineEdit_dhcpip.setObjectName("lineEdit_dhcpip")
        
        self.lineEdit_dhcpuser = QtWidgets.QLineEdit(self.groupBox_connect)
        self.lineEdit_dhcpuser.setGeometry(QtCore.QRect(324, 47, 151, 22))
        self.lineEdit_dhcpuser.setObjectName("lineEdit_dhcpuser")
        
        self.label_dhcpuser = QtWidgets.QLabel(self.groupBox_connect)
        self.label_dhcpuser.setGeometry(QtCore.QRect(283, 42, 91, 31))
        self.label_dhcpuser.setObjectName("label_dhcpuser")
        
        self.lineEdit_dhcppwd = QtWidgets.QLineEdit(self.groupBox_connect)
        self.lineEdit_dhcppwd.setGeometry(QtCore.QRect(610, 48, 151, 22))
        self.lineEdit_dhcppwd.setObjectName("lineEdit_dhcppwd")
        
        self.label_dhcppwd = QtWidgets.QLabel(self.groupBox_connect)
        self.label_dhcppwd.setGeometry(QtCore.QRect(548, 44, 51, 31))
        self.label_dhcppwd.setObjectName("label_dhcppwd")
        
        self.pushButton_dhcpconnect = QtWidgets.QPushButton(self.groupBox_connect)
        self.pushButton_dhcpconnect.setGeometry(QtCore.QRect(860, 80, 93, 28))
        self.pushButton_dhcpconnect.setObjectName("pushButton_dhcpconnect")
        
        self.groupBox_dhcplog = QtWidgets.QGroupBox(self.dhcpcofig)
        self.groupBox_dhcplog.setGeometry(QtCore.QRect(480, 150, 511, 531))
        self.groupBox_dhcplog.setObjectName("groupBox_dhcplog")
        
        self.textEdit_dhcplog = QtWidgets.QTextEdit(self.groupBox_dhcplog)
        self.textEdit_dhcplog.setGeometry(QtCore.QRect(10, 20, 481, 481))
        self.textEdit_dhcplog.setObjectName("textEdit_dhcplog")
        
        self.configpage.addTab(self.dhcpcofig, "")
        self.FTP = QtWidgets.QWidget()
        self.FTP.setObjectName("FTP")
        
        self.groupBox_connect_ftp = QtWidgets.QGroupBox(self.FTP)
        self.groupBox_connect_ftp.setGeometry(QtCore.QRect(20, 40, 991, 121))
        self.groupBox_connect_ftp.setObjectName("groupBox_connect_ftp")
        
        self.label_ftpip = QtWidgets.QLabel(self.groupBox_connect_ftp)
        self.label_ftpip.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.label_ftpip.setObjectName("label_ftpip")
        
        self.lineEdit_ftpip = QtWidgets.QLineEdit(self.groupBox_connect_ftp)
        self.lineEdit_ftpip.setGeometry(QtCore.QRect(96, 45, 151, 22))
        self.lineEdit_ftpip.setObjectName("lineEdit_ftpip")
        
        self.lineEdit_ftpuser = QtWidgets.QLineEdit(self.groupBox_connect_ftp)
        self.lineEdit_ftpuser.setGeometry(QtCore.QRect(324, 47, 151, 22))
        self.lineEdit_ftpuser.setObjectName("lineEdit_ftpuser")
        
        self.label_ftpuser = QtWidgets.QLabel(self.groupBox_connect_ftp)
        self.label_ftpuser.setGeometry(QtCore.QRect(283, 42, 91, 31))
        self.label_ftpuser.setObjectName("label_ftpuser")
        
        self.lineEdit_ftppwd = QtWidgets.QLineEdit(self.groupBox_connect_ftp)
        self.lineEdit_ftppwd.setGeometry(QtCore.QRect(610, 48, 151, 22))
        self.lineEdit_ftppwd.setObjectName("lineEdit_ftppwd")
        
        self.label_ftppwd = QtWidgets.QLabel(self.groupBox_connect_ftp)
        self.label_ftppwd.setGeometry(QtCore.QRect(548, 44, 51, 31))
        self.label_ftppwd.setObjectName("label_ftppwd")
        
        self.pushButton_ftpconnect = QtWidgets.QPushButton(self.groupBox_connect_ftp)
        self.pushButton_ftpconnect.setGeometry(QtCore.QRect(860, 80, 93, 28))
        self.pushButton_ftpconnect.setObjectName("pushButton_ftpconnect")
        
        self.treeWidget = QtWidgets.QTreeWidget(self.FTP)
        self.treeWidget.setGeometry(QtCore.QRect(20, 198, 256, 491))
        self.treeWidget.setObjectName("treeWidget")
        
        self.lineEdit_ftp = QtWidgets.QLineEdit(self.FTP)
        self.lineEdit_ftp.setGeometry(QtCore.QRect(330, 200, 471, 22))
        self.lineEdit_ftp.setObjectName("lineEdit_ftp")
        
        self.pushButton_browse = QtWidgets.QPushButton(self.FTP)
        self.pushButton_browse.setGeometry(QtCore.QRect(880, 200, 93, 28))
        self.pushButton_browse.setObjectName("pushButton_browse")
        
        self.pushButton_upload = QtWidgets.QPushButton(self.FTP)
        self.pushButton_upload.setGeometry(QtCore.QRect(880, 250, 93, 28))
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.configpage.addTab(self.FTP, "")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))
        self.menubar.setObjectName("menubar")        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.configpage.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ok.setText(_translate("MainWindow", "Finsih"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.groupBox_checkpoint.setTitle(_translate("MainWindow", "Check Point"))
        self.checkBox_network.setText(_translate("MainWindow", "Network"))
        self.checkBox_tsport.setText(_translate("MainWindow", "Terminal port"))
        self.checkBox_cpri.setText(_translate("MainWindow", "CPRI "))
        self.checkBox_iqdata.setText(_translate("MainWindow", "IQdata "))
        self.label_netstatus.setText(_translate("MainWindow", "Net status"))
        self.label_tpstatus.setText(_translate("MainWindow", "TP status"))
        self.label_cpristatus.setText(_translate("MainWindow", "CPRI status"))
        self.label_iqstatus.setText(_translate("MainWindow", "IQdata status"))
        self.pushButton_check.setText(_translate("MainWindow", "Check"))
        self.groupBox_configpoint.setTitle(_translate("MainWindow", "Run Scripts"))
        self.groupBox_cfgnetwork.setTitle(_translate("MainWindow", "Config Network"))
        self.label_configip.setText(_translate("MainWindow", "IP:"))
        self.label_gateway.setText(_translate("MainWindow", "Gateway:"))
        self.pushButton_cfgnetsub.setText(_translate("MainWindow", "Submit"))
        self.label_DNS.setText(_translate("MainWindow", "DNS:"))
        self.groupBox_cfgterminal.setTitle(_translate("MainWindow", "Config Terminal server"))
        self.label_tspos.setText(_translate("MainWindow", "POS :"))
        self.label_tsip.setText(_translate("MainWindow", "TS IP :"))
        self.label_tsports.setText(_translate("MainWindow", "TS PORT :"))
        self.pushButton_cfgtssub.setText(_translate("MainWindow", "Submit"))
        self.groupBox_cfgruma.setTitle(_translate("MainWindow", "Config RUMA"))
        self.label_rumapos.setText(_translate("MainWindow", "POS :"))
        self.label_rumaip.setText(_translate("MainWindow", "RUMA IP :"))
        self.label_rumaports.setText(_translate("MainWindow", "RUMA PORT :"))
        self.pushButton_cfgrumasub.setText(_translate("MainWindow", "Submit"))
        self.groupBox_log.setTitle(_translate("MainWindow", "Result"))
        self.connection.setTitle(_translate("MainWindow", "Connection"))
        self.label_user.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">User:</span></p></body></html>"))
        self.label_serverip.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Server IP:</span></p></body></html>"))
        self.label_port.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Port:</span></p></body></html>"))
        self.pushButton_stpconnection.setText(_translate("MainWindow", "Connection"))
        self.groupBox_session.setTitle(_translate("MainWindow", "Session Choice"))
        self.radioButton_ssh.setText(_translate("MainWindow", "SSH"))
        self.radioButton_telnet.setText(_translate("MainWindow", "TELENT"))
        self.radioButton_ct11.setText(_translate("MainWindow", "RUMA"))
        self.label_passwd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Passwd:</span></p></body></html>"))
        self.configpage.setTabText(self.configpage.indexOf(self.stpconfig), _translate("MainWindow", "STP CONFIG"))
        self.groupBox_dhcpconfig.setTitle(_translate("MainWindow", "DHCP config"))
        self.groupBox_add.setTitle(_translate("MainWindow", "IP info"))
        self.label_addip.setText(_translate("MainWindow", "IP :"))
        self.label_addmac.setText(_translate("MainWindow", "MAC:"))
        self.label_addhostname.setText(_translate("MainWindow", "Hostname :"))
        self.pushButton_cfgok.setText(_translate("MainWindow", "Submit"))
        self.pushButton_cfgcancel.setText(_translate("MainWindow", "Cancel"))
        self.groupBox_configchoice.setTitle(_translate("MainWindow", "Config"))
        self.radioButton_search.setText(_translate("MainWindow", "Search"))
        self.radioButton_del.setText(_translate("MainWindow", "Delete"))
        self.radioButton_add.setText(_translate("MainWindow", "Add"))
        self.radioButton_modify.setText(_translate("MainWindow", "Modify"))
        self.radioButton_backup.setText(_translate("MainWindow", "Backup"))
        self.groupBox_connect.setTitle(_translate("MainWindow", "Connection"))
        self.label_dhcpip.setText(_translate("MainWindow", "DHCP server:"))
        self.label_dhcpuser.setText(_translate("MainWindow", "User:"))
        self.label_dhcppwd.setText(_translate("MainWindow", "Passwd :"))
        self.pushButton_dhcpconnect.setText(_translate("MainWindow", "Connect"))
        self.groupBox_dhcplog.setTitle(_translate("MainWindow", "Console"))
        self.configpage.setTabText(self.configpage.indexOf(self.dhcpcofig), _translate("MainWindow", "DHCP CONFIG"))
        self.groupBox_connect_ftp.setTitle(_translate("MainWindow", "Connection"))
        self.label_ftpip.setText(_translate("MainWindow", "FTP server:"))
        self.label_ftpuser.setText(_translate("MainWindow", "User:"))
        self.label_ftppwd.setText(_translate("MainWindow", "Passwd :"))
        self.pushButton_ftpconnect.setText(_translate("MainWindow", "Connect"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))
        self.pushButton_upload.setText(_translate("MainWindow", "Upload"))
        self.configpage.setTabText(self.configpage.indexOf(self.FTP), _translate("MainWindow", "FTP"))
    
    
    
    



        
        
    
if __name__ == "__main__":
    #app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
    #window= query_window()
    #window.show()
    #sys.exit(app.exec_())
    pass
