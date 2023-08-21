# see https://mypy.readthedocs.io/en/stable/runtime_troubles.html
from __future__ import annotations
# avoid circular imports at runtime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from snowpiercer.resources.resource import Resource
    from snowpiercer.agents.agent import Agent
from typing import List

class Conflict:
    contested_ressource : Resource = None
    agents_involved : List[Agent] = []
    
    def __init__(self, contested_ressource : Resource, agents_involved : List[Agent]):
        self.contested_ressource = contested_ressource
        self.agents_involved = agents_involved
        
    # str method
    def __str__(self):
        #TODO: implement
        pass
    
    def add_agent_involved(self, agent: Agent):
        self.agents_involved.append(agent)

    def remove_agent_involved(self, agent: Agent):
        self.agents_involved.remove(agent)