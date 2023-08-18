from .ressource import Ressource
from ...agents import Agent

class Appel(Ressource):

    nutrition = 0.3

    def consumed_by(self, agent: Agent):
        return agent.feed(self.nutrition)