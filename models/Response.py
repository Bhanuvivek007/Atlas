from dataclasses import dataclass


@dataclass(frozen=True)
class Response:
    message: str
    follow_ups: list[str]
