'''
Created on Aug 18, 2019

@author: eguxcha
'''
import sys
#import dhcpcfg
from autoconfigUI import Ui_MainWindow
from dialogUI import Ui_dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QInputDialog,QMessageBox,QDialog
import backend.log
import backend.dhcp
import operations.dhcp
import backend.hosts
import logging
LOGGER = logging.getLogger(__name__)
backend.log.config_logger()

DHCP_HOST = 'nj_lab_dhcp'


class mainwindow(QtWidgets.QMainWindow,Ui_MainWindow):
    sig_search = pyqtSignal()
    sig_add = pyqtSignal()
    sig_mod = pyqtSignal()
    sig_del = pyqtSignal()
    sig_backup = pyqtSignal()
    def __init__(self, parent=None):
        super(mainwindow, self).__init__(parent)
        self.setupUi(self)
        
        #search ip
        self.radioButton_search.clicked.connect(self.dhcpsearch)
        #self.sig_search.connect(self.sig_searchip)
        
        #add ip
        self.radioButton_add.clicked.connect(self.dhcpadd)
        #self.sig_add.connect(self.sig_addip)

        #modify ip
        self.radioButton_modify.clicked.connect(self.dhcpmod)
        #self.sig_mod.connect(self.sig_modip)
        
        #delete ip
        self.radioButton_del.clicked.connect(self.dhcpdel)
        #self.sig_del.connect(self.sig_delip)
        
        #backup ip
        self.radioButton_backup.clicked.connect(self.dhcpbackup)
        self.sig_backup.connect(self.sig_backupip)
        self.pushButton_dhcpconnect.clicked.connect(self.DHCP_connect)
        self.pushButton_cfgok.clicked.connect(self.radiobutton_dhcpconfig)
        self.pushButton_cfgcancel.clicked.connect(self.closewindow)

        
    def dhcpsearch(self):
        self.sig_search.emit()
    
    def dhcpadd(self):
        self.sig_add.emit()
    
    def dhcpmod(self):
        self.sig_mod.emit()
    
    def dhcpdel(self):
        self.sig_del.emit()
        
    def dhcpbackup(self):
        #self.sig_backupip.emit()
        pass
        
    def sig_searchip(self):
        self.getIPinfo_DHCP()
        print("start to search from config file")
        found_host = None
        if self.ip_dhcp:
            self.log("search by ip :" + self.ip_dhcp)
            try:
                found_host = self.subnet.get_host_by_ip(self.ip_dhcp)
                self.log(str(found_host))
            except backend.dhcp.HostNotFound:
                self.log("Ip not found")
        elif self.hostname_dhcp:
            self.log("search by hostname:" + self.hostname_dhcp)
            try:
                found_host = self.subnet.get_host_by_hostname(self.hostname_dhcp)
                self.log(str(found_host))
            except backend.dhcp.HostNotFound:
                self.log('Hostname not found')
        elif self.mac_dhcp:
            self.log("search by mac:" + self.mac_dhcp)
            try:
                found_host = self.subnet.get_host_by_mac(self.mac_dhcp)
                self.log(str(found_host))
            except backend.dhcp.HostNotFound:
                self.log("Mac not found")
        else:
            self.log("Error: Please provide ip or hostname")
            QMessageBox.information(self, "Error", "Please provide ip or hostname")
            return
        print("found_host     ", found_host)
        return found_host
    
    def sig_addip(self):
        self.log("checke if this new host existed")
        self.getIPinfo_DHCP()
        if self.ip_dhcp and self.hostname_dhcp and self.mac_dhcp:
            pass
        else:
            self.log("Please provide new hostname, ip and mac")
            QMessageBox.information(self, "Error", "Please provide new hostname, ip and mac")
            return
        if self.sig_searchip():
            self.log("This host is already in config file, no need to add")
            QMessageBox.information(self, "Error", "This host is already in config file, no need to add")
            return
        else:
            self.log("This new host is not in config file, start to add it in.")
            new_host = backend.dhcp.HostConfig(hostname=self.hostname_dhcp,
                                               declarations=['hardware ethernet ' + self.mac_dhcp + ';',
                                                             'fixed-address ' + self.ip_dhcp + ';'])
            self.log(str(new_host))
            self.subnet.add_host(new_host)
            self.log("Search this new host in config file to check if add succeed")
            try:
                found_host = self.subnet.get_host_by_hostname(self.hostname_dhcp)
                self.log(str(found_host))
                self.log("Add successfully")
                QMessageBox.information(self, "Info", "Add successfully")
            except backend.dhcp.HostNotFound:
                self.log("Add failed")
                QMessageBox.information(self, "Error", "Add failed")
                return

    def sig_modip(self):
        self.mod = dialogwindow()
        self.mod.buttonBox.accepted.connect(self.modify_dialog)
        self.mod.show()

    def sig_delip(self):
        self.getIPinfo_DHCP()
        del_host = False
        if self.ip_dhcp or self.hostname_dhcp:
            pass
        else:
            self.log("Please provide ip or hostname")
            QMessageBox.information(self, "Error", "Please provide ip or hostname")
            return
        print('sssss', self.sig_searchip())
        if self.sig_searchip():
            self.log("This host is already in config file, you can remove it")
            if self.ip_dhcp:
                self.log("Remove host by ip")
                self.subnet.remove_host_by_ip(self.ip_dhcp)
                try:
                    found_host = self.subnet.get_host_by_ip(self.ip_dhcp)
                    self.log(str(found_host))
                    self.log('Failed to remove host')
                    QMessageBox.information(self, "Error", "Failed to remove host")
                    return
                except backend.dhcp.HostNotFound:
                    self.log('Removed successfully')
                    QMessageBox.information(self, "Info", "Removed successfully")
                    del_host = True
            elif self.hostname_dhcp:
                self.log("Remove host by hostname")
                self.subnet.remove_host_by_name(self.hostname_dhcp)
                try:
                    found_host = self.subnet.get_host_by_hostname(self.hostname_dhcp)
                    self.log(str(found_host))
                    self.log('Failed to remove host')
                    QMessageBox.information(self, "Error", "Failed to remove host")
                    return
                except backend.dhcp.HostNotFound:
                    self.log('Removed successfully')
                    QMessageBox.information(self, "Info", "Removed successfully")
                    del_host = True
        else:
            self.log("This host can't be found, no need to remove")
            QMessageBox.information(self, "Error", "This host can't be found, no need to remove")
            return
        return del_host

    def sig_backupip(self):
        result = operations.dhcp.backup_dhcp_config(self.connection)
        self.log(result)

    def DHCP_server(self):
        self.dhcpip = self.lineEdit_dhcpip.text()
        self.dhcpuser = self.lineEdit_dhcpuser.text()
        self.dhcppwd = self.lineEdit_dhcppwd.text()
        print("Connecting Server {}@{}..., password: {}".format(self.dhcpuser, self.dhcpip, self.dhcppwd))

    def log(self, message):
        self.textEdit_dhcplog.append(message)

    def DHCP_connect(self):
        self.connection = backend.hosts.get_connection(DHCP_HOST)
        dhcp_config_str = operations.dhcp.get_dhcp_config(self.connection)
        dhcp_config = backend.dhcp.DhcpConfig.from_string(dhcp_config_str)

        LOGGER.info('查找子网')
        self.subnet = dhcp_config.get_subnet(subnet_number='10.186.198.0')
        self.log(dhcp_config_str)

    def closewindow(self):
        print("exit...")
        sys.exit(0)

    def getIPinfo_DHCP(self):
        self.ip_dhcp = self.lineEdit_addip.text()
        self.mac_dhcp = self.lineEdit_addmac.text()
        self.hostname_dhcp = self.lineEdit_addhostname.text()

    def check_input(self):
        if self.ip_dhcp or self.mac_dhcp or self.hostname_dhcp:
            self.check = True
        else:
            self.check = False
        return self.check

    def radiobutton_dhcpconfig(self):
        if self.radioButton_search.isChecked():
            self.log("checked search")
            QMessageBox.information(self, "info", "Search?", QMessageBox.Yes | QMessageBox.No)
            self.sig_searchip()
        if self.radioButton_add.isChecked():
            self.log("checked add")
            QMessageBox.information(self, "info", "Add?", QMessageBox.Yes | QMessageBox.No)
            self.sig_addip()
        if self.radioButton_del.isChecked():
            self.log("checked delete")
            QMessageBox.information(self, "info", "Delete?", QMessageBox.Yes | QMessageBox.No)
            self.sig_delip()
        if self.radioButton_modify.isChecked():
            self.log("checked modify")
            QMessageBox.information(self, "info", "Modify?", QMessageBox.Yes | QMessageBox.No)
            self.sig_modip()
        if self.radioButton_backup.isChecked():
            self.log("checked backup")
            QMessageBox.information(self, "info", "Backup?", QMessageBox.Yes | QMessageBox.No)
            self.sig_backupip()

    def modify_dialog(self):
        print("get value from child window:{}".format(self.mod.lineEdit_addhost.text()))
        print("get value from child window:{}".format(self.mod.lineEdit_addIP.text()))
        print("get value from child window:{}".format(self.mod.lineEdit_addMAC.text()))
        if self.mod.lineEdit_addhost.text() and self.mod.lineEdit_addIP.text() \
                and self.mod.lineEdit_addMAC.text():
            pass
        else:
            self.log("Error: please provide new hostname, ip and mac")
            QMessageBox.information(self, "Error", "please provide new hostname, ip and mac")
            return

        if self.sig_delip():
            self.log("Remove old host successfully, start to add new host in")
            new_host = backend.dhcp.HostConfig(hostname=self.mod.lineEdit_addhost.text(),
                                               declarations=['hardware ethernet ' +
                                                             self.mod.lineEdit_addMAC.text(),
                                                             'fixed-address ' +
                                                             self.mod.lineEdit_addIP.text()])

            print("new host:{}".format(new_host))
            self.subnet.add_host(new_host)
            try:
                found_host = self.subnet.get_host_by_hostname(self.mod.lineEdit_addhost.text())
                self.log(str(found_host))
                self.log('New Host found,Modify succeed')
                QMessageBox.information(self, "Info", "New Host found, Modify succeed")
            except backend.dhcp.HostNotFound:
                self.log('Hostname not found,Modify failed')
                QMessageBox.information(self, "Error", "New Host not found, Modify failed")
                return


class dialogwindow(QDialog, Ui_dialog):
    mySignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(dialogwindow, self).__init__(parent)
        self.setupUi(self)
        self.addhostname = ""
        self.addip = ""
        self.addmac = ""
    
    def dialogok(self):
        self.addhostname = self.lineEdit_addhost.text()
        self.addip =self.lineEdit_addIP.text()
        self.addmac =self.lineEdit_addMAC.text()
        print("hostname :{}".format(self.addhostname))
        print("IP :{}".format(self.addip))
        print("MAC :{}".format(self.addmac))

    def dialogcancel(self):
        sys.exit(0)
    
def ui_main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())

 
if __name__ == '__main__':
    ui_main()
