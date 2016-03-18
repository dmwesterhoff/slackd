"""
slackd.commands.users
~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import operator
import click
import tabulate
from common.slack_client import slack_client


@click.command()
def users():
    """List all of the team's users and their status"""
    try:
        response = slack_client.users.list(presence=True)
    except Exception as e:
        click.echo(str(e))

    if response.successful:
        users = response.body['members']

        # Collect array of arrays that contain user data in column order
        table_data = []
        for user in users:
            if not user['deleted']:
                user_data = [user['name'],
                             user.get('real_name', None),
                             user.get('presence', 'bot'),
                             user['profile'].get('email', None)]
                table_data.append(user_data)
        table_data.sort(key=operator.itemgetter(2))
        table_headers = [click.style('User', fg='yellow'),
                         click.style('Name', fg='yellow'),
                         click.style('Presence', fg='yellow'),
                         click.style('Email', fg='yellow')]
        click.secho(tabulate.tabulate(table_data,
                                      table_headers,
                                      tablefmt="fancy_grid"))
    else:
        click.secho('wtf')
