from typing import List

from environment import Environment
from agents import Agent
from environment.resources import Resource
from conflicts import ConflictResolver

class World:
    environment : Environment = None
    agents : List[Agent] = []
    resolve_strategy : ConflictResolver = None
    resources : List[Resource] = []
    
    def get_population_size(self):
        return len(self.agents)