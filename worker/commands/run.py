"""
The run command is meant to start the server and the
connection towards the message queue.
"""

import click
from worker.settings import app_settings


@click.group(name="run")
def run():
    pass


@run.command
def hello_world():
    click.echo("Worker service started...")
    click.echo(f"Configured with Panorama {app_settings.panos_host}")
    click.confirm("Press any key to exit.")


@run.command
def server():
    raise NotImplementedError
