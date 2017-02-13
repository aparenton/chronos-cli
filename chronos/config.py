from collections import namedtuple
from os import path

import yaml

from chronos.exceptions import ChronosException


DEFAULT_CONFIG_FILES = ['~/.config/chronos/config.json',
                        '~/.config/chronos/config.yaml',
                        '~/.config/chronos/config.yml']

Server = namedtuple('Server', ['name', 'url', 'username', 'password'])


def load_server(profile_names, config=None):
    if not config:
        for default_path in DEFAULT_CONFIG_FILES:
            if path.exists(path.expanduser(default_path)):
                config = path.expanduser(default_path)
                break
        else:
            raise ChronosException('No config file exists under ~/.config/chronos')
    with open(config, 'r') as fp:
        config = yaml.load(fp.read())
        for profile in reversed(profile_names):
            if profile in config:
                server_config = config[profile]
                return Server(profile, server_config['url'], server_config['username'], server_config['password'])
