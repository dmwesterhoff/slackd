"""
slackd.commands.channels
~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import operator
import click
import tabulate
from common.slack_client import slack_client
from common.readable_bool import readable_bool


@click.command()
def channels():
    """List all available channels for the team"""
    try:
        response = slack_client.channels.list()
    except Exception as e:
        click.secho(str(e))

    if response.successful:
        channels = response.body['channels']

        table_data = []
        for channel in channels:
            data = [channel['name'],
                    channel['is_member'],
                    channel['num_members']]
            table_data.append(data)
        table_data.sort(key=operator.itemgetter(2), reverse=True)

        for data in table_data:
            data[1] = readable_bool(data[1])

        table_headers = [click.style('Name', fg='yellow'),
                         click.style('Member?', fg='yellow'),
                         click.style('Members', fg='yellow')]
        click.secho(tabulate.tabulate(table_data,
                                      table_headers,
                                      tablefmt="fancy_grid"))

    else:
        click.secho('wtf')
