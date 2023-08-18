from .agent import Agent

class NormieAgent(Agent):
    
    def __init__(self, reproduction_rate):
        self.reproduction_rate = reproduction_rate
    
    def placeholder_method(self):
        print("I'm a normie")
        print("My reproduction rate is", self.reproduction_rate)