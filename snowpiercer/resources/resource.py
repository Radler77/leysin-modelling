# see https://mypy.readthedocs.io/en/stable/runtime_troubles.html
from __future__ import annotations
# avoid circular imports at runtime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from snowpiercer.agents.agent import Agent

from abc import ABC, abstractmethod


class Resource(ABC):
    type: str = None

    @abstractmethod
    def consumed_by(self, agent: Agent):
        pass

    @abstractmethod
    def get_type(self):
        pass
