"""
slackd.commands.open
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import click
import webbrowser
from common.slack_client import slack_client


@click.command()
def open():
    """Opens a new browser window to the user's Slack homepage"""
    try:
        response = slack_client.auth.test()
    except Exception as e:
        click.echo(str(e))

    if response.successful:
        url = response.body['url']
        webbrowser.open(url)
    else:
        click.echo('wtf')
