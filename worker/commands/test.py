'''
"test" command group for testing the API interaction with
the Panorama environment. This set of commands is meant to
help troubleshooting what the automated process would do
with involving a message queue.
'''

from ipaddress import IPv4Address
import click

from worker import services
from worker.settings import app_settings


@click.group(name="test")
@click.pass_context
def test_group(ctx: click.Context):
    pass


@test_group.command
@click.pass_context
def get_dynamic_user_group(ctx: click.Context):
    raise NotImplementedError


@test_group.command
@click.pass_context
def add_dynamic_user_group_mapping(ctx: click.Context):
    raise NotImplementedError


@test_group.command
@click.pass_context
def remove_dynamic_user_group_mapping(ctx: click.Context):
    raise NotImplementedError


@test_group.command(name="login-user")
@click.argument("user")
@click.argument("ip")
@click.option("--timeout")
def login_user(
    user: str,
    ip: IPv4Address,
    timeout: int
):
    firewall = services.panos.connect_to_firewall(
        host=app_settings.panos_host,
        port=app_settings.panos_port,
        username=app_settings.panos_username,
        password=app_settings.panos_password,
    )

    services.firewall.login_user(firewall, user, ip, timeout)
    click.echo(f"User {user} registered successfully with IP {ip}.")


@test_group.command
@click.pass_context
def remove_user_ip_mapping(ctx: click.Context):
    raise NotImplementedError
