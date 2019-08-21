# -*- coding:utf-8 -*-
from fabric import Connection
import telnetlib
import logging
import time


LOGGER = logging.getLogger(__name__)
 
class SetConnection():
    def __init__(self,):
        self.tn = telnetlib.Telnet()
        
    def sshconn(self,host_ip,user,port,passwd):
        try:
            sshconnect = Connection(host_ip,user,port,connect_kwargs={"password":passwd})
            return sshconnect
        except:
            LOGGER.debug('%s ssh network connect error' %host_ip)
            return  False
    
    def telnetconn(self,host_ip,connport,username,passwd):
        try:
            self.tn.open(host_ip,connport)
        except:
            LOGGER.warning('%s telnet network connect error' %host_ip)
            return  False
        self.tn.read_until(b'login: ',timeout=10)
        self.tn.write(username.encode('ascii') + b'\n')   
        self.tn.read_until(b'Password: ',timeout=10)
        self.tn.write(passwd.encode('ascii') + b'\n')
        time.sleep(1)
        command_result = self.tn.read_very_eager().decode('ascii')
        if 'Login incorrect' not in command_result:
            logging.warning('%s connect success'%host_ip)
            return True
        else:
            logging.warning('%s connect failed'%host_ip)
            return False

    def execute_command(self,command):
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(1)
        command_result = self.tn.read_very_eager().decode('ascii')
        #logging.warning('execute_result：\n%s' % command_result)
        print(command_result)
        
    def logout_host(self):
        self.tn.write(b"exit\n")
     
       
    
def restart(connect, slot=None, delay=0, wait_for_complete=True, wait_for_onm=True, timeout=600):
        if delay > 0:
            time.sleep(delay)

        if slot is None:
            connect.run('restart')
        else:
            connect.run('restart {}'.format(slot))

        if wait_for_complete:
            connect.wait_for_reboot(timeout=timeout)

        if wait_for_onm:
            connect.wait_for_onm()
def wait_for_onm(connect, timeout=600):
        LOGGER.debug('Waiting for onm.')
        start_time = time.time()
        while time.time() - start_time < timeout:
            output = connect.run('trdc')
            if 'Usage: trdc' in output:
                break
            time.sleep(3)
        else:
            raise RuntimeError('Timed out while waiting for for O&M')
        
def runlmc(connect):
        connect.run("ll")
        connect.run("ip -a")


if __name__ == '__main__':
    host_ip = '10.186.133.167'
    username = 'root'
    connport = '23'
    passwd = 'njwmlaod'
    command = 'ports'
    command1 = 'plf li li'
    
    #a = basictest.BasicTestFution()
    setconn = SetConnection()
    if setconn.sshconn(host_ip,username,connport,passwd):
       conn1 = setconn.sshconn(host_ip,username,connport,passwd)
       runlmc(conn1)
       
    if setconn.telnetconn(host_ip,connport,username,passwd):
        setconn.execute_command(command)
        setconn.execute_command(command1)
        setconn.logout_host()
        
    
    