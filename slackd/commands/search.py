"""
slackd.commands.search
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import click
from common.slack_client import slack_client


@click.group(invoke_without_command=True)
@click.pass_context
def search(ctx):
    """Searches slack for both files and messages, or if supplied with a
    subcommand will filter to one or the other."""
    if ctx.invoked_subcommand is None:
        try:
            response = slack_client.search.all()
            if response.successful:
                data = response.body
                print data
        except Exception as e:
            print str(e)


@click.command()
def messages():
    try:
        response = slack_client.search.messages()
        if response.successful:
            data = response.body
            print data
    except Exception as e:
        print str(e)


@click.command()
def files():
    try:
        response = slack_client.search.files()
        if response.successful:
            data = response.body
            print data
    except Exception as e:
        print str(e)


search.add_command(messages)
search.add_command(files)
