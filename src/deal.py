"""Real-estate deal."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from agent import Agent
from bank import Bank
from buyer import Buyer
from seller import Seller


@dataclass
class Deal:
    id: int
    date: str
    status: str = field(default="Нова")

    # Aggregation: deal keeps references to participants (they can exist independently).
    seller: Optional[Seller] = None
    buyer: Optional[Buyer] = None
    agent: Optional[Agent] = None
    bank: Optional[Bank] = None

    def confirm(self) -> None:
        print(f"Угода #{self.id} підтверджена")
        self.status = "Підтверджена"

    def cancel(self) -> None:
        print(f"Угода #{self.id} скасована")
        self.status = "Скасована"

    def set_seller(self, seller: Seller) -> None:
        self.seller = seller

    def set_buyer(self, buyer: Buyer) -> None:
        self.buyer = buyer

    def set_agent(self, agent: Agent) -> None:
        self.agent = agent

    def set_bank(self, bank: Bank) -> None:
        self.bank = bank
