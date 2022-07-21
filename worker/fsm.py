"""
FSM implementation to process the messages received on the
message queue.
"""
import logging
import json

import pika
from pydantic import ValidationError

from worker.models import Message
from worker import paloalto


LOGGER = logging.getLogger(__name__)


class StateUnknownError(Exception):
    pass


class SimpleConsumer:
    STATES = (
        ("userid.login", "login"),
        ("userid.logout", "logout"),
        ("userid.tag", "tag"),
        ("userid.untag", "untag"),
    )

    def __init__(self, host, username, password, queue_name):
        connection_parameters = pika.ConnectionParameters(
            host=host,
            credentials=pika.PlainCredentials(username, password)
        )

        self._connection = pika.BlockingConnection(connection_parameters)
        self._channel = self._connection.channel()
        self._channel.basic_consume(queue_name, self.on_message)

    def _deserialize(self, body: bytes):
        payload = json.loads(body.decode())
        return Message(**payload)

    def _dispatch_event(self, message: Message):
        method, = (state[1] for state in self.STATES
                   if state[0 == message.event])

        LOGGER.info(f"Method found: {method}")

        getattr(paloalto, (self.STATES[method]))(message)

    def on_message(self, channel, method_frame, header_frame, body):
        """ Message processing from RAbbitMQ queue."""
        LOGGER.info(body)
        try:
            message = self._deserialize(body)

            if message.event not in (state[0] for state in self.STATES):
                raise StateUnknownError

            self._dispatch_event(message)
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)

        except ValidationError:
            LOGGER.error("Message body validation error.")
        except StateUnknownError:
            LOGGER.error("The received message doesn't have a valid event.")

    def run(self):
        try:
            self._channel.start_consuming()
        except KeyboardInterrupt:
            self._channel.stop_consuming()
        finally:
            self._connection.close()
