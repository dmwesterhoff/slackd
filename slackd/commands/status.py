"""
slackd.commands.status
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import click
from common.slack_client import slack_client


@click.command()
def status():
    """Shows status of the currently authed user if a Slack API Token has
    been properly provided"""
    try:
        response = slack_client.auth.test()
    except Exception as e:
        click.echo(str(e))

    if response.successful:
        data = response.body
        username = data['user']
        team = data['team']
        url = data['url']
        click.secho("User: ", nl=False, fg='yellow')
        click.secho("{} ".format(username))
        # click.secho("({})".format(user_id))
        click.secho("Team: ", nl=False, fg='yellow')
        click.secho("{} ".format(team))
        # click.secho("({})".format(team_id))
        click.secho("Home: ", nl=False, fg='yellow')
        click.secho("{} ".format(url), underline=True)
    else:
        click.echo('wtf')
