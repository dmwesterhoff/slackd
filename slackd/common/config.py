"""
slackd.common.config
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import os
import ConfigParser

CONFIG_FILE_PATH = '~/.slackd.cfg'


def config_dictionary():
    """Returns the config variables as a python dictionary"""
    config = ConfigParser.RawConfigParser()
    with open(os.path.expanduser('~/.slackd.cfg'), 'r') as configfile:
        config.readfp(configfile)

    options = config.options('slackd')
    dictionary = {}
    for option in options:
        try:
            dictionary[option] = config.get('slackd', option)
        except Exception as e:
            print str(e)
            dictionary[option] = None
    return dictionary


def create_config(token):
    """Creates a new config parser file with the slack api token, the
    other values are defaulted until overidden by the end user"""
    config = ConfigParser.RawConfigParser()
    config.add_section('slackd')
    config.set('slackd', 'token', token)
    with open(os.path.expanduser('~/.slackd.cfg'), 'wb') as configfile:
        config.write(configfile)


def read_config_token():
    """Returns the slack token that has previously been set in the config"""
    config = ConfigParser.RawConfigParser()
    with open(os.path.expanduser('~/.slackd.cfg'), 'r') as configfile:
        config.readfp(configfile)

    try:
        return config.get('slackd', 'token')
    except Exception as e:
        print str(e)
        return None
