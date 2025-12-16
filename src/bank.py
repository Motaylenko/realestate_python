"""Bank participant."""

from __future__ import annotations

from participant import Participant


class Bank(Participant):
    def __init__(self, name: str, contact_info: str) -> None:
        super().__init__(name, contact_info)

    def evaluate_mortgage(self) -> bool:
        print(f"Банк {self.name} оцінює можливість надання іпотеки")
        return True  # Імітація позитивного рішення
