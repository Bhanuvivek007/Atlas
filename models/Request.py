from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Optional
from uuid import UUID


class RequestSource(Enum):
    CLI = auto()
    VOICE = auto()
    API = auto()


@dataclass(frozen=True)
class Request:
    id: UUID
    text: str
    source: RequestSource
    session_id: Optional[UUID]
    timestamp: datetime
