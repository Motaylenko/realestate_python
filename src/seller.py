"""Seller of a property."""

from __future__ import annotations

from participant import Participant
from reviewable import Reviewable


class Seller(Participant, Reviewable):
    def __init__(self, name: str, contact_info: str, property_: str) -> None:
        super().__init__(name, contact_info)
        self.property = property_

    def counter_offer(self) -> None:
        print(f"Продавець {self.name} зробив зустрічну пропозицію щодо {self.property}")

    def review_offer(self) -> None:
        print(f"Продавець {self.name} переглядає пропозицію")
