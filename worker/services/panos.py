"""
The panos service takes care of the communication with PAN-OS
and Panorama and is responsible for sending the XML API calls 
using the pan-os-python SDK.
"""

import logging
from panos import panorama

logger = logging.getLogger()


def connect_to_panorama(host: str, username: str, password: str, port: int = 443):
    """ Returns a connection handler to Panorama"""
    try:
        logger.info(f"Connecting to Panorama instance {host}:{port}")
        return panorama.Panorama(host, username, password, port=port)
    except Exception as e:
        logger.exception("There was an error while connecting to panorama.", stack_info=True)
        raise e


def get_dynamic_user_group(handler: panorama.Panorama, name: str):
    """ Gets a dynamcic user group using the connection handler"""
    raise NotImplemented

def create_dynamic_user_group(handler: panorama.Panorama, name: str):
    """ Creates a dynamcic user group using the connection handler"""
    raise NotImplemented


def add_user_to_dynamic_user_group(handler: panorama.Panorama, name: str, user: str):
    """ Adds a new user to a specific DUG"""
    raise NotImplemented


def remove_user_to_dynamic_user_group(handler: panorama.Panorama, name: str, user: str):
    """ Adds a new user to a specific DUG"""
    raise NotImplemented

