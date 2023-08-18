from abc import ABC, abstractmethod

class Resource(ABC):
    
    @abstractmethod
    def consumed_by(self, agent: Agent):
        pass