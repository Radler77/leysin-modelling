from snowpiercer.resources.resource import Resource
from snowpiercer.agents.agent import Agent


class AppleTree(Resource):
    apples_per_turn = 5

    def consumed_by(self, agent: Agent):
        return agent.change_shelter_quality(0.5)

    def get_type(self):
        return "wood"
    
    def get_apples_per_turn(self):
        return self.apples_per_turn
