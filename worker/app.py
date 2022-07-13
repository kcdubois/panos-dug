import click

from worker.commands.test import test_group
from worker.commands.run import run


@click.group
def cli():
    pass


cli.add_command(test_group)
cli.add_command(run)
