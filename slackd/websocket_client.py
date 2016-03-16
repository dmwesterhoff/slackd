#!/usr/bin/env python

"""
slackd.webscoket_client
~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import websocket
import slack_requests
import thread
import time


def on_message(ws, message):
    print message


def on_error(ws, error):
    print "[!] Socket error: {}".format(error)


def on_close(ws):
    print "[!] Socket closed"


def on_open(ws):
    print "[!] Socket opened"


if __name__ == '__main__':
    websocket.enableTrace(True)
    rtm_start_response = slack_requests.rtm_start()
    ws = websocket.WebSocketApp(rtm_start_response.json()['url'],
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
