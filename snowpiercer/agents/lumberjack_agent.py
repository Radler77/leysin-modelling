from random import Random
from typing import List, Optional
from snowpiercer.conflicts.conflict import Conflict
from snowpiercer.resources.resource import Resource
from snowpiercer.agents.agent import Agent


class LumberjackAgent(Agent):
    random = Random()

    def __init__(self, initial_shelter_quality: float = 0.0):
        self.shelter_quality = initial_shelter_quality

    def reproduce(self):
        return LumberjackAgent(self.shelter_quality)

    def initial_resource_selection(self, resources: List[Resource]) -> Optional[Resource]:
        wood_resources = list(filter(lambda r: r.get_type() == "wood", resources))
        food_resources = list(filter(lambda r: r.get_type() == "food", resources))

        if len(wood_resources) == 0:
            if len(food_resources) > 0:
                return self.random.choice(food_resources)
            return None

        chance_of_taking_wood = (1 - self.shelter_quality) * (0.54 + self.satiety * 0.5 - (1 / (len(wood_resources))))

        choose_wood = self.random.random() < chance_of_taking_wood

        if choose_wood and len(wood_resources) > 0:
            return self.random.choice(wood_resources)
        elif len(food_resources) > 0:
            return self.random.choice(food_resources)
        return None

    def handle_conflict(self, conflict: Conflict):
        # I won't give up my contested resource, no matter what
        return
