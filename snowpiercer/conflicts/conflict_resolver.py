# see https://mypy.readthedocs.io/en/stable/runtime_troubles.html
from __future__ import annotations
# avoid circular imports at runtime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from snowpiercer.agents import Agent
    from snowpiercer.conflicts import Conflict
    from snowpiercer.resources import Resource

from abc import ABC, abstractmethod


class ConflictResolver(ABC):

    @abstractmethod
    def resolve_conflict(self, conflicts: list[Conflict]) -> dict[Agent, Resource]:
        pass
