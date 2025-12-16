"""Entry point (converted from Main.java)."""

from __future__ import annotations

from agent import Agent
from bank import Bank
from buyer import Buyer
from deal import Deal
from seller import Seller


def main() -> None:
    # Створення учасників
    buyer = Buyer("Іван Петренко", "ivan@email.com", 10000.0)
    seller = Seller("Марія Коваленко", "maria@email.com", "Квартира на Хрещатику")
    agent = Agent("Олег Сидоренко", "oleg@email.com", "Київська Нерухомість")
    bank = Bank("ПриватБанк", "office@privatbank.ua")

    # Створення угоди
    deal = Deal(1, "2025-10-20")
    deal.set_buyer(buyer)
    deal.set_seller(seller)
    deal.set_agent(agent)
    deal.set_bank(bank)

    # Демонстрація процесу
    print("\n=== Демонстрація роботи програми ===\n")

    agent.organize_tour()
    agent.show_property()

    buyer.send_proposal()
    seller.review_offer()
    seller.counter_offer()

    if bank.evaluate_mortgage():
        buyer.finalize_deal()
        deal.confirm()
    else:
        deal.cancel()


if __name__ == "__main__":
    main()
