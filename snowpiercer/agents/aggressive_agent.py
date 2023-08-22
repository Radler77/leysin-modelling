from random import Random
from typing import List, Optional
from snowpiercer.conflicts.conflict import Conflict
from snowpiercer.resources.resource import Resource
from snowpiercer.agents.agent import Agent


class AggressiveAgent(Agent):
    random = Random()

    def reproduce(self):
        return AggressiveAgent()

    def initial_resource_selection(self, resources: List[Resource]) -> Optional[Resource]:
        return self.random.choice(resources)

    def handle_conflict(self, conflict: Conflict):
        # I won't give up my contested resource, no matter what
        return
