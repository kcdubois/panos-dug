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
    rabbitmq_host: str = "rabbitmq"
    rabbitmq_user: str = "guest"
    rabbitmq_password: str = "guest"
    rabbitmq_exchange_name: str = "panos_worker"
    rabbitmq_queue_name: str = "userid"


app_settings = Settings()
