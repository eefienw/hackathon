import lark
import re

MAC_REGEX = r'[0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}'


class BaseConfig:
    pass


class SubnetNotFound(RuntimeError):
    pass


class HostNotFound(RuntimeError):
    pass


class DhcpConfig(BaseConfig):
    DHCP_CONFIG_GRAMMER = r"""
        start: ( COMMENT | NEWLINE | subnet | host | parameter )+

        subnet: "subnet" NAME "netmask" NAME "{" NEWLINE* ( parameter | COMMENT | host | NEWLINE )+ "}" NEWLINE
        host: "host" NAME "{" NEWLINE* ( parameter | COMMENT )+ "}" NEWLINE
        parameter: NAME+  ";" NEWLINE
    
        COMMENT: /#[^\n]*/ NEWLINE
        NAME: ESCAPED_STRING | /(?!subnet |host )[\w\-_:.]+/ 
        NEWLINE: /\r?\n[\t ]*/

        //%import common.WS
        %import common.ESCAPED_STRING
        //%ignore WS
        %ignore /[\t \f]+/
    """

    def __init__(self, config):
        self._config = config

        pass

    @classmethod
    def from_string(cls, config_str: str):
        if config_str[-1] != '\n':
            config_str += '\n'
        parser = lark.Lark(cls.DHCP_CONFIG_GRAMMER)
        return cls.from_tree(parser.parse(config_str))

    @classmethod
    def from_tree(cls, config_tree: lark.Tree):
        config = []
        for i in config_tree.children:
            if isinstance(i, lark.Token):
                config.append(str(i).strip())
            elif isinstance(i, lark.Tree):
                if i.data == 'parameter':
                    config.append(ParameterConfig.from_tree(i))
                elif i.data == 'subnet':
                    config.append(SubnetConfig.from_tree(i))
                else:
                    raise RuntimeError()
            else:
                raise RuntimeError()
        return cls(config)

    @property
    def subnets(self) -> list:
        return list(filter(lambda x: isinstance(x, SubnetConfig), self._config))

    def get_subnet(self, subnet_number: str) -> 'SubnetConfig':
        for subnet_config in self.subnets:
            if subnet_number == subnet_config.subnet_number:
                return subnet_config
        raise SubnetNotFound()

    def __str__(self):
        return '\n'.join([str(i) for i in self._config])


class ParameterConfig(BaseConfig):
    def __init__(self, parameter):
        self._parameter = parameter

    @classmethod
    def from_tree(cls, config_tree):
        return ParameterConfig(' '.join([str(i) for i in config_tree.children]).strip())

    def __str__(self):
        return self._parameter + ';'


class SubnetConfig(BaseConfig):
    def __init__(self, subnet_number, netmask, children):
        self._subnet_number = subnet_number
        self._netmask = netmask
        self._children = children

    @classmethod
    def from_tree(cls, config_tree):
        subnet_number = config_tree.children[0]
        netmask = config_tree.children[1]
        children = []
        for i in config_tree.children[2:]:
            if isinstance(i, lark.Token):
                children.append(str(i).strip())
            elif isinstance(i, lark.Tree):
                if i.data == 'parameter':
                    children.append(ParameterConfig.from_tree(i))
                elif i.data == 'host':
                    children.append(HostConfig.from_tree(i))
                else:
                    raise RuntimeError()
            else:
                raise RuntimeError()
        if children[0] == '':
            children.pop(0)
        if children[-1] == '':
            children.pop()
        return cls(subnet_number, netmask, children)

    @property
    def subnet_number(self):
        return self._subnet_number

    @property
    def hosts(self) -> list:
        return list(filter(lambda x: isinstance(x, HostConfig), self._children))

    def get_host_by_hostname(self, hostname: str) -> 'HostConfig':
        for host_config in self.hosts:
            if hostname == host_config.hostname:
                return host_config
        raise HostNotFound()

    def get_host_by_ip(self, ip: str):
        for host_config in self.hosts:
            if ip == host_config.ip_address:
                return host_config
        raise HostNotFound()

    def get_host_by_mac(self, mac: str):
        for host_config in self.hosts:
            if mac == host_config.mac:
                return host_config
        raise HostNotFound()

    def add_host(self, host_config: 'HostConfig'):
        self._children.append(host_config)

    def remove_host_by_name(self, hostname: str):
        self._children = list(
            filter(lambda x: isinstance(x, HostConfig) and x.hostname != hostname, self._children))

    def remove_host_by_ip(self, ip: str):
        self._children = list(
            filter(lambda x: isinstance(x, HostConfig) and x.ip_address != ip, self._children))

    def __str__(self):
        internal = '\n'.join([str(i) for i in self._children])
        internal = '\n'.join(['    ' + i for i in internal.splitlines()])
        return f'subnet {self._subnet_number} netmask {self._netmask} {{\n{internal}\n}}'


class HostConfig(BaseConfig):
    def __init__(self, hostname, declarations: list = None):
        self._hostname = hostname
        if declarations is None:
            self._declarations = []
        else:
            self._declarations = declarations

    @classmethod
    def from_tree(cls, config_tree):
        hostname = config_tree.children[0]
        children = []
        for i in config_tree.children[1:]:
            if isinstance(i, lark.Token):
                children.append(str(i).strip())
            elif isinstance(i, lark.Tree):
                if i.data == 'parameter':
                    children.append(ParameterConfig.from_tree(i))
                else:
                    raise RuntimeError()
            else:
                raise RuntimeError()
        if children[0] == '':
            children.pop(0)
        if children[-1] == '':
            children.pop()
        return cls(hostname, children)

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, hostname: str):
        self._hostname = hostname

    @property
    def declarations(self):
        return self._declarations[:]

    @declarations.setter
    def declarations(self, declarations: list):
        self._declarations = declarations

    @property
    def ip_address(self):
        for i in self.declarations:
            matches = re.findall(r'fixed-address ([\d.]+)', str(i))
            if matches:
                return matches[0]
        else:
            raise HostNotFound()


    @property
    def mac(self):
        for i in self.declarations:
            matches = re.findall(r'hardware \w+ ((?:[a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2})', str(i))
            if matches:
                return matches[0]
        else:
            raise HostNotFound()

    def __str__(self):
        internal = '\n'.join([str(i) for i in self._declarations])
        internal = '\n'.join(['    ' + i for i in internal.splitlines()])

        return f'host {self._hostname} {{\n{internal}\n}}'
