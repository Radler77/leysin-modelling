from random import Random
from typing import List, Optional
from snowpiercer.conflicts.conflict import Conflict
from snowpiercer.resources.resource import Resource
from snowpiercer.agents.agent import Agent


class NormieAgent(Agent):
    random = Random()

    # choose any resource of type "food" if the agent is not fully satiated
    def initial_resource_selection(self, resources: List[Resource]) -> Optional[Resource]:
        if self.satiety >= 1:
            return None

        food: List[Resource] = list(filter(lambda resource: resource.get_type() == "food", resources))
        index: int = self.random.randint(0, len(food) - 1)

        return food[index]

    def handle_conflict(self, conflict: Conflict):
        # give up the contested resource if i can survive without it and another agent wants to consume it
        if self.get_basic_need_fulfillment() >= self.survival_threshold and len(conflict.agents_involved) >= 2:
            conflict.agents_involved.remove(self)

    def reproduce(self):
        return NormieAgent()
