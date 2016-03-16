#!/usr/bin/env python

"""
slackd.webscoket_client
~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import json
from pygments import highlight, lexers, formatters


def pretty_json(json_object):
    """Accepts a python dictionary and returns pretty printed JSON string"""
    formatted_json = None
    if type(json_object) is dict:
        formatted_json = json.dumps(json_object,
                                    indent=4,
                                    sort_keys=True)
    elif type(json_object) is list:
        formatted_json = json.dumps(json_object,
                                    indent=4)

    colorful_json = highlight(unicode(formatted_json, 'UTF-8'),
                              lexers.JsonLexer(),
                              formatters.TerminalFormatter())
    return colorful_json
