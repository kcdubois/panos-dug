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


def tag_user(
    handler: firewall.Firewall,
    user: str,
    tag: str,
    timeout: int = 1440
):
    """ Adds a new user to a specific DUG"""
    try:
        handler.userid.tag_user(user, [tag], timeout=timeout)
    except Exception as e:
        logger.exception(f"Can't register user tag: {e}")
        raise


def untag_user(
    handler: firewall.Firewall,
    user: str,
    tag: str
):
    """ Adds a new user to a specific DUG"""
    try:
        handler.userid.untag_user(user, [tag])
    except Exception as e:
        logger.exception(f"Can't unregister user tag: {e}")
        raise


def login_user(
    handler: firewall.Firewall,
    user: str,
    ip: IPv4Address,
    timeout: int = None
):
    """ Create a user-ip mapping """
    try:
        login_timeout = timeout or app_settings.panos_userid_timeout
        logging.info(f"Creating login mapping {user}/{ip}/{timeout}")

        handler.userid.login(user, str(ip), login_timeout)
    except Exception as e:
        logger.exception(f"An error occured while logging in a user. {e}")
        raise


def logout_user(handler: firewall.Firewall, user: str, ip: IPv4Address):
    """ Remove a user-ip mapping """
    try:
        logging.info(f"Removing user mapping {user}/{ip}")

        handler.userid.logout(user, str(ip))
    except Exception as e:
        logger.exception(f"An error occured while logging in a user. {e}")
        raise
