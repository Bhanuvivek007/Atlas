from dataclasses import dataclass
from enum import Enum, auto


class TeachingStrategy(Enum):
    EXPLAIN = auto()
    SOCRATIC = auto()
    QUIZ = auto()
    REVIEW = auto()
    DEBUG = auto()


@dataclass(frozen=True)
class TeachingPlan:
    goal: str
    strategy: TeachingStrategy
    instructions: list[str]
