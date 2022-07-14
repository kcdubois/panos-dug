'''
"test" command group for testing the API interaction with
the Panorama environment. This set of commands is meant to
help troubleshooting what the automated process would do
with involving a message queue.
'''

from ipaddress import IPv4Address
import click

from worker.services import paloalto
from worker.settings import app_settings


@click.group(name="test")
def test_group():
    pass


@test_group.command(name="tag")
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


@test_group.command(name="untag")
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


@test_group.command(name="login")
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


@test_group.command(name="logout")
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


test_group.add_command(tag_user)
test_group.add_command(untag_user)
test_group.add_command(login_user)
test_group.add_command(logout_user)
