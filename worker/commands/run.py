"""
The run command is meant to start the server and the 
connection towards the message queue.
"""

import click
from worker.settings import settings


@click.command
def run():
    raise NotImplemented