#!/usr/bin/env python

"""
slackd.common.readable_bool
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""


def readable_bool(b):
    """Takes a boolean variable and returns "yes" for true and "no" for false
    as a string object.

    :param b: boolean variable to use
    """
    if b:
        return "yes"
    else:
        return "no"
