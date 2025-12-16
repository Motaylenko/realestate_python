"""Base participant of a real-estate deal.

In Java this is an abstract class.
"""

from __future__ import annotations

from abc import ABC


class Participant(ABC):
    def __init__(self, name: str, contact_info: str) -> None:
        self.name = name
        self.contact_info = contact_info

    def get_info(self) -> str:
        return f"Ім'я: {self.name}, Контакти: {self.contact_info}"
