from abc import ABC, abstractmethod
from agents import Agent

class Resource(ABC):
    
    @abstractmethod
    def consumed_by(self, agent: Agent):
        pass

    def get_type(self):
        return "generic"