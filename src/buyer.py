"""Buyer of a property."""

from __future__ import annotations

from typing import final

from participant import Participant


class Buyer(Participant):
    def __init__(self, name: str, contact_info: str, deposit: float) -> None:
        super().__init__(name, contact_info)
        self.deposit = float(deposit)

    def send_proposal(self) -> None:
        print(f"Покупець {self.name} надіслав пропозицію")

    @final
    def finalize_deal(self) -> None:
        # "final" in Python is enforced by type-checkers (mypy/pyright), not at runtime.
        print(f"Покупець {self.name} завершує угоду. Завдаток: {self.deposit}")
