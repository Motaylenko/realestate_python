"""Real-estate agent."""

from __future__ import annotations

from participant import Participant
from reviewable import Reviewable


class Agent(Participant, Reviewable):
    def __init__(self, name: str, contact_info: str, agency: str) -> None:
        super().__init__(name, contact_info)
        self.agency = agency

    def organize_tour(self) -> None:
        print(f"Агент {self.name} з {self.agency} організовує 3D-тур")

    def show_property(self) -> None:
        print(f"Агент {self.name} показує нерухомість")

    def review_offer(self) -> None:
        print(f"Агент {self.name} переглядає пропозицію")
