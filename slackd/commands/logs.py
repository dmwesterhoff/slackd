"""
slackd.commands.logs
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import click
from common.slack_client import slack_client

@click.command()
def logs():
    """Displays the access logs for the team"""
    click.secho('logs')


@click.command()
def ilogs():
    """Displays the integration logs for the team"""
    click.secho('ilogs')
