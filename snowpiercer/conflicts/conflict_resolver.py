from abc import ABC, abstractmethod

from agents import Agent
from conflicts.conflict import Conflict
from environment.resources import Resource


class ConflictResolver(ABC):

    @abstractmethod
    def resolve_conflict(self, conflicts: list[Conflict]) -> dict[Agent, Resource]:
        pass
