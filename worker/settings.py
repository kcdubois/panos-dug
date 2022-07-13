"""
Settings are meant to be globally available across the application
without passing objects all around as an input parameter.
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    panos_host: str
    panos_port: int = None
    panos_username: str
    panos_password: str
    panos_userid_timeout: int = 60


app_settings = Settings()
