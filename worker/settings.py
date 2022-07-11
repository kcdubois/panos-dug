from ast import Str
from asyncio import streams
from lib2to3.pytree import Base
"""
Settings are meant to be globally available across the application
without passing objects all around as an input parameter.
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    panorama_host: str
    panorama_port: int
    panorama_username: str
    panorama_password: str
    dug_name: str


settings = Settings()