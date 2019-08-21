import json
import pathlib

import fabric

HOST_CONFIG_DIR = pathlib.Path(__file__).parent.parent / 'hosts'


def get_connection(host, **kwargs):
    target_json = f'{host}.json'
    json_file = None
    for host_config in HOST_CONFIG_DIR.glob('*.json'):
        if host_config.name == target_json:
            json_file = host_config
            break

    if json_file:
        with json_file.open() as fp:
            host_config = json.load(fp)
        host = host_config.pop('hostname', host)
        username = host_config.pop('username', None)
        my_connect_kwargs = host_config
        my_connect_kwargs.update(kwargs.get('connect_kwargs', {}))
        my_kwargs = {'user': username}
        my_kwargs.update(kwargs)
        my_kwargs['connect_kwargs'] = my_connect_kwargs
        kwargs = my_kwargs

    return fabric.Connection(host=host, **kwargs)
