from pydantic import BaseModel
from typing import Optional


class Message(BaseModel):
    event: str
    ip: Optional[str] = None
    user: Optional[str] = None
