"""
The panos service takes care of the communication with PAN-OS
and Panorama and is responsible for sending the XML API calls
using the pan-os-python SDK.
"""

import logging

from panos import firewall
from panos.errors import PanDeviceXapiError

from worker.settings import app_settings


LOGGER = logging.getLogger(__name__)


class PanService:
    def __init__(self, host: str, user: str, password: str, port: int = 443):
        try:
            LOGGER.info(f"Connecting to PAN-OS instance {host}:{port}")
            self.handler = firewall.Firewall(
                host,
                user,
                password,
                port=port
            )
        except Exception:
            LOGGER.exception("There was an error while connecting to PAN-OS.")
            raise

    def tag_user(self, user: str, tag: str, timeout: int = 1440):
        """ Adds a new user to a specific DUG"""
        try:
            self.handler.userid.tag_user(user, [tag], timeout=timeout)
        except Exception as e:
            LOGGER.exception(f"Can't register user tag: {e}")
            raise

    def untag_user(self, user: str, tag: str):
        """ Adds a new user to a specific DUG"""
        try:
            self.handler.userid.untag_user(user, [tag])
        except Exception as e:
            LOGGER.exception(f"Can't unregister user tag: {e}")
            raise

    def login(self, user: str, ip: str, timeout: int = 3600):
        """ Create a user-ip mapping """
        try:
            login_timeout = timeout or app_settings.panos_userid_timeout
            logging.info(f"Creating login mapping {user}/{ip}/{timeout}")

            self.handler.userid.login(user, str(ip), login_timeout)
        except PanDeviceXapiError as e:
            LOGGER.exception(f"An error occured while logging in a user. {e}")

    def logout(self, user: str, ip: str):
        """ Remove a user-ip mapping """
        try:
            logging.info(f"Removing user mapping {user}/{ip}")

            self.handler.userid.logout(user, str(ip))
        except Exception as e:
            LOGGER.exception(f"An error occured while logging in a user. {e}")
            raise
