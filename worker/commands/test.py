'''
"test" command group for testing the API interaction with
the Panorama environment. This set of commands is meant to
help troubleshooting what the automated process would do 
with involving a message queue.
'''

import click

@click.group(name="test")
@click.pass_context
def test_group(ctx: click.Context):
    pass


@test_group.command
@click.pass_context
def get_dynamic_user_group(ctx: click.Context):
    raise NotImplemented


@test_group.command
@click.pass_context
def add_dynamic_user_group_mapping(ctx: click.Context):
    raise NotImplemented


@test_group.command
@click.pass_context
def remove_dynamic_user_group_mapping(ctx: click.Context):
    raise NotImplemented


@test_group.command
@click.pass_context
def add_user_ip_mapping(ctx: click.Context):
    raise NotImplemented


@test_group.command
@click.pass_context
def remove_user_ip_mapping(ctx: click.Context):
    raise NotImplemented