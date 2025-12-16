"""Reviewable "interface".

In Java this is an interface; in Python we model it with an abstract base class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Reviewable(ABC):
    @abstractmethod
    def review_offer(self) -> None:
        """Review an offer/proposal."""
        raise NotImplementedError
