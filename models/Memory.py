from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from uuid import UUID


class MemoryCategory(Enum):
    IDENTITY = auto()
    LEARNING = auto()
    PROJECT = auto()
    OBSERVATION = auto()


@dataclass
class Memory:
    id: UUID
    content: str
    category: MemoryCategory
    confidence: float
    created_at: datetime
    last_accessed_at: datetime
