from .resource import Resource
from ...agents import Agent


class Apple(Resource):
    nutrition = 0.3

    def consumed_by(self, agent: Agent):
        return agent.eat(self.nutrition)

    def get_type(self):
        return "food"
