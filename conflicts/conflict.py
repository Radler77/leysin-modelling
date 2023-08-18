from typing import List
from environment.resources import Resource
from agents import Agent

class Conflict:
    contested_ressource : Resource = None
    agents_involved : List[Agent] = []
    
    def __init__(self, contested_ressource : Resource, agents_involved : List[Agent]):
        self.contested_ressource = contested_ressource
        self.agents_involved = agents_involved