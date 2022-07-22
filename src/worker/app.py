import logging
from ipaddress import IPv4Address

import click

from worker import fsm, paloalto
from worker.settings import app_settings


LOGGER = logging.getLogger(__name__)


@click.group
def cli():
    pass


@cli.command
def run():
    logging.basicConfig(level=logging.DEBUG)
    try:
        LOGGER.info("Starting the RabbitMQ consumer.")
        pan_service = paloalto.PanService(
            app_settings.panos_host,
            app_settings.panos_username,
            app_settings.panos_password,
            app_settings.panos_port
        )

        consumer = fsm.SimpleConsumer(
            app_settings.rabbitmq_host,
            app_settings.rabbitmq_user,
            app_settings.rabbitmq_password,
            app_settings.rabbitmq_queue_name,
            pan_service
        )

        consumer.run()
    finally:
        LOGGER.info("Stopped the RabbitMQ consumer.")


@cli.group(name="test")
def test():
    pass


@test.command(name="tag")
@click.argument("user")
@click.argument("tag")
@click.option("--timeout")
def tag_user(user: str, tag: str, timeout=1440):
    firewall = paloalto.connect_to_firewall(
        host=app_settings.panos_host,
        port=app_settings.panos_port,
        username=app_settings.panos_username,
        password=app_settings.panos_password,
    )

    paloalto.tag_user(firewall, user, tag, timeout)
    click.echo(f"User {user} registered successfully with tag {tag}.")


@test.command(name="untag")
@click.argument("user")
@click.argument("tag")
def untag_user(user: str, tag: str):
    firewall = paloalto.connect_to_firewall(
        host=app_settings.panos_host,
        port=app_settings.panos_port,
        username=app_settings.panos_username,
        password=app_settings.panos_password,
    )

    paloalto.untag_user(firewall, user, tag)
    click.echo(f"User {user} unregistered successfully with tag {tag}.")


@test.command(name="login")
@click.argument("user")
@click.argument("ip")
@click.option("--timeout")
def login_user(
    user: str,
    ip: IPv4Address,
    timeout: int
):
    firewall = paloalto.connect_to_firewall(
        host=app_settings.panos_host,
        port=app_settings.panos_port,
        username=app_settings.panos_username,
        password=app_settings.panos_password,
    )

    paloalto.login_user(firewall, user, ip, timeout)
    click.echo(f"User {user} registered successfully with IP {ip}.")


@test.command(name="logout")
@click.argument("user")
@click.argument("ip")
def logout_user(user: str, ip: IPv4Address):
    firewall = paloalto.connect_to_firewall(
        host=app_settings.panos_host,
        port=app_settings.panos_port,
        username=app_settings.panos_username,
        password=app_settings.panos_password,
    )

    paloalto.logout_user(firewall, user, str(ip))
    click.echo(f"User {user} unregistered successfully with IP {ip}.")
