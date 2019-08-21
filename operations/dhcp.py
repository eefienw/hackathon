import tempfile
import datetime
from backend.hosts import get_connection


def get_dhcp_config(connection: 'Connection') -> str:
    result = connection.run('cat /etc/dhcp/dhcpd.conf')
    return result.stdout[:-1]


def backup_dhcp_config(connection: 'Connection') -> str:
    backup_filename = 'dhcpd_' + datetime.datetime.now().isoformat() + '.conf'
    cmd1 = 'cp -r /etc/dhcp/dhcpd.conf /tmp/' + backup_filename
    connection.run(cmd1)
    cmd2 = 'ls -al /tmp/' + backup_filename
    result = connection.run(cmd2)
    return result.stdout[:-1]


def upload_dhcp_config(connection: 'Connection', dhcp_config):
    if not isinstance(dhcp_config, str):
        dhcp_config = str(dhcp_config)
    with tempfile.TemporaryFile('r+') as fp:
        fp.write(dhcp_config)
        fp.seek(0)
        connection.put(fp, '/tmp/dhcp_testing')


def restart_dhcp_service(connection: 'Connection'):
    connection.sudo('service isc-dhcp-server restart')
