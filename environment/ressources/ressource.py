from abc import ABC, abstractmethod

class Ressource(ABC):
    
    @abstractmethod
    def consumed_by(self, agent: Agent):
        pass