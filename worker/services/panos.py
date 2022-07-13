"""
The panos service takes care of the communication with PAN-OS
and Panorama and is responsible for sending the XML API calls
using the pan-os-python SDK.
"""

from ipaddress import IPv4Address
import logging

from panos import firewall

from worker.settings import app_settings


logger = logging.getLogger()


def connect_to_firewall(
    host: str,
    username: str,
    password: str,
    port: int = 443
):
    """ Returns a connection handler to firewall"""
    try:
        logger.info(f"Connecting to Panorama instance {host}:{port}")
        return firewall.Firewall(host, username, password, port=port)
    except Exception as e:
        logger.exception("There was an error while connecting to panorama.",
                         stack_info=True)
        raise e


def get_dynamic_user_group(handler: firewall.Firewall, name: str):
    """ Gets a dynamcic user group using the connection handler"""
    raise NotImplementedError


def create_dynamic_user_group(handler: firewall.Firewall, name: str):
    """ Creates a dynamcic user group using the connection handler"""
    raise NotImplementedError


def add_user_to_dynamic_user_group(
    handler: firewall.Firewall,
    name: str,
    user: str
):
    """ Adds a new user to a specific DUG"""
    raise NotImplementedError


def remove_user_to_dynamic_user_group(
    handler: firewall.Firewall,
    name: str,
    user: str
):
    """ Adds a new user to a specific DUG"""
    raise NotImplementedError


def login_user(
    handler: firewall.Firewall,
    user: str,
    ip: IPv4Address,
    timeout: int = None
):
    """ Create a user-ip mapping """
    try:
        login_timeout = timeout | app_settings.panos_userid_timeout
        logging.info(f"Creating login mapping {user}/{ip}/{timeout}")

        handler.userid.login(user, str(ip), login_timeout)
    except Exception as e:
        logger.exception(f"An error occured while logging in a user. {e}")


def logout_user(handler: firewall.Firewall, user: str, ip: IPv4Address):
    """ Remove a user-ip mapping """
    try:
        logging.info(f"Removing user mapping {user}/{ip}")

        handler.userid.logout(user, str(ip))
    except Exception as e:
        logger.exception(f"An error occured while logging in a user. {e}")
