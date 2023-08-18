from abc import ABC, abstractmethod

class Agent(ABC):
    reproduction_rate = 0.0

    @abstractmethod
    def placeholder_method(self):
        pass