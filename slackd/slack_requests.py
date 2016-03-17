#!/usr/bin/env python

"""
slackd.slack_requests
~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import os
import requests


# Auth
# ~~~~
def auth():
    """Makes a request to determine if a user is authenticated with their
    slack token and if so will return identity information"""
    token = os.environ['SLACK_TOKEN']
    return requests.post('https://slack.com/api/auth.test',
                         params={'token': token})


# Channels
# ~~~~~~~~
def list_channels():
    """This method returns a list of all channels in the team"""
    token = os.environ['SLACK_TOKEN']
    return requests.post('https://slack.com/api/channels.list',
                         params={'token': token})


def create_channel(name):
    """Creates a new channel for the team with specified name, requires
    the scope 'channels:write'

    :param name: Name to create the channel as
    """
    token = os.environ['SLACK_TOKEN']
    return requests.post('https://slack.com/api/channels.create',
                         params={'token': token,
                                 'name': name})


# Chat
# ~~~~
def post_message(channel, message):
    """Sends a message to the given (DM) channel or the group specified

    :param channel: The channel id to post the message to
    :param message: The text to send to the channel
    """
    token = os.environ['SLACK_TOKEN']
    return requests.post('https://slack.com/api/users.list',
                         params={'token': token,
                                 'channel': channel,
                                 'text': message,
                                 'as_user': True})


# Team
# ~~~~
def access_logs(count=100, page=1):
    """Returns Slack access logs on the team

    :param count: (optional) Number of items to return
    :param page: (optional) Page number of results to return
    """
    token = os.environ['SLACK_TOKEN']
    return requests.post('https://slack.com/api/team.accessLogs',
                         params={'token': token,
                                 'count': count,
                                 'page': page})


# Real-Time Messaging
# ~~~~~~~~~~~~~~~~~~~
def rtm_start():
    """Makes a request to the slack real time messaging start endpoint
    which returns data on the current state of authed user as well as a
    short-lived websocket entry endpoint. The call returns a Response object
    or will raise a requests exception if something went wrong. The access
    token used should be in the OS environment keyed as 'SLACK_TOKEN'
    """
    token = os.environ['SLACK_TOKEN']
    return requests.post('https://slack.com/api/rtm.start',
                         params={'token': token})


# Users
# ~~~~~
def list_users():
    """This method returns a list of all users on the team"""
    token = os.environ['SLACK_TOKEN']
    return requests.post('https://slack.com/api/users.list',
                         params={'token': token,
                                 'presence': True})
