from .resource import Resource
from ...agents import Agent


class Apple(Resource):
    type = "food"
    nutrition = 0.3

    def consumed_by(self, agent: Agent):
        return agent.eat(self.nutrition)
