from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class Session:
    id: UUID
    title: Optional[str]
    started_at: datetime
    last_active_at: datetime
