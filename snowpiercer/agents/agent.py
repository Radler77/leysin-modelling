from abc import ABC, abstractmethod
from typing import List, Optional

from snowpiercer.conflicts.conflict import Conflict
from snowpiercer.resources.resource import Resource


class Agent(ABC):
    satiety = .5
    shelter_quality = .0

    # minimum basic_need_fulfillment that an Agent needs to survive
    survival_threshold = .3

    # minimum basic_need_fulfillment that an Agent needs to reproduce
    reproduction_threshold = 0.7

    def get_basic_need_fulfillment(self):
        return self.satiety * (self.shelter_quality * 0.1 + 0.95)

    def change_satiety(self, amount: float):
        self.satiety = min(1.0, self.satiety + amount)

    def change_shelter_quality(self, amount: float):
        self.shelter_quality = min(1.0, self.shelter_quality + amount)

    def can_reproduce(self) -> bool:
        return self.get_basic_need_fulfillment() > self.reproduction_threshold

    def can_survive(self) -> bool:
        return self.get_basic_need_fulfillment() > self.survival_threshold

    def next_timestep(self):
        self.change_satiety(-0.1 * (1 - self.shelter_quality))

    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def initial_resource_selection(self, resources: List[Resource]) -> Optional[Resource]:
        pass

    @abstractmethod
    def handle_conflict(self, conflict: Conflict):
        pass
