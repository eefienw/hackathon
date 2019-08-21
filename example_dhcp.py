import backend.dhcp
import backend.hosts
import backend.log
import operations.dhcp
import logging

LOGGER = logging.getLogger(__name__)
backend.log.config_logger()

DHCP_HOST = 'nj_lab_dhcp'

if __name__ == '__main__':
    connection = backend.hosts.get_connection(DHCP_HOST)

    LOGGER.info('下载DHCP配置')
    dhcp_config_str = operations.dhcp.get_dhcp_config(connection)
    dhcp_config_str = open('dhcpd.conf').read()
    dhcp_config = backend.dhcp.DhcpConfig.from_string(dhcp_config_str)

    LOGGER.info('查找子网')
    subnet = dhcp_config.get_subnet(subnet_number='10.186.198.0')
    assert subnet.subnet_number == '10.186.198.0'

    # Debug
    print('Debug')
    host = subnet.get_host_by_ip('10.186.198.18')

    print(host)

    LOGGER.info('新建 host statement')
    new_host = backend.dhcp.HostConfig(hostname='New-Host',
                                       declarations=['hardware ethernet AA:AA:AA:AA:AA:AA',
                                                     'fixed-address 10.186.133.53'])
    #LOGGER.log(new_host)
    print(new_host)
    subnet.add_host(new_host)

    LOGGER.info('查找刚创建的Host')
    found_host = subnet.get_host_by_hostname('New-Host')
    print(found_host)
    assert found_host.hostname == 'New-Host'

    LOGGER.info('修改Host')
    old_host = new_host
    old_host.hostname = 'Modified-Host'
    found_host = subnet.get_host_by_hostname('Modified-Host')
    print(found_host)

    LOGGER.info('删除Host')
    subnet.remove_host('Modified-Host')
    try:
        subnet.get_host_by_hostname('Modified-Host')
        LOGGER.error('Failed to remove host')
    except backend.dhcp.HostNotFound:
        pass

    LOGGER.info('上传配置')
    # operations.dhcp.upload_dhcp_config(connection, dhcp_config)

    LOGGER.info('重启服务')
    # operations.dhcp.restart_dhcp_service(connection)
