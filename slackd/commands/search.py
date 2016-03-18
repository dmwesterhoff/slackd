"""
slackd.commands.search
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 David M. Westerhoff
:license: All rights reserved

"""

import click


@click.group(invoke_without_command=True)
@click.pass_context
def search(ctx):
    """Searches slack for both files and messages, or if supplied with a
    subcommand will filter to one or the other."""
    if ctx.invoked_subcommand is None:
        click.secho('search')


@click.command()
def messages():
    click.secho('messages only')


@click.command()
def files():
    click.secho('files only')


search.add_command(messages)
search.add_command(files)
