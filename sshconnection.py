# -*- coding:utf-8 -*-
from fabric import Connection
import logging
import time

HOST="root@10.186.133.57"
USER="root"
PORT=22
CONNECTIONTIMEOUT=100
CONNECT_KWARGS="njwmload"
LOGGER = logging.getLogger(__name__)
 
def sshconn(host,connpwd):
    connect = Connection(host,connect_kwargs={"password": connpwd})
    return connect
    
def exc_command1(sshconn):
    with sshconn.cd('/etc'):
        sshconn.run("cat resolv.conf")
        sshconn.run("pwd")
        sshconn.run("df -h")
    with sshconn.cd('/nas/results/executions/'):
         sshconn.run('ls -l')
def exc_command2(sshconn):
    with sshconn.cd('/'):
        sshconn.run("pwd")
def exc_command3(sshconn):
        sshconn.run("lmclist")
        sshconn.run("par get")
        sshconn.run('help')
        sshconn.run('ricr -s')
             
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
        connect.run("ifconfig")
        



if __name__ == '__main__':
    conn1=sshconn(HOST, CONNECT_KWARGS)
    #a = basictest.BasicTestFution()
    runlmc(conn1)
    
    
    
    