from abc import ABC, abstractmethod
from agents import Agent

class Resource(ABC):
    type : str = None
    
    @abstractmethod
    def consumed_by(self, agent: Agent):
        pass