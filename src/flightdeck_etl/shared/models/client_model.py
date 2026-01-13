from pydantic import BaseModel
from dataclasses import dataclass
import datetime


class Client(BaseModel):
    client_id: int
    name: str
    website: str


@dataclass
class Task:
    id: int
    description: str
    due_date: datetime.date
    owner_id: int
