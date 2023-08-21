from typing import List

from environment import Environment
from agents import Agent
from environment.resources import Resource
from conflicts import ConflictResolver


class World:
    environment: Environment = None
    agents: List[Agent] = []
    resolve_strategy: ConflictResolver = None
    resources: List[Resource] = []

    def get_population_size(self):
        return len(self.agents)

    def next_time_step(self):
        self.environment.next_time_step()
        next_agents: List[Agent] = []
        for agent in self.agents:
            if agent.can_reproduce():
                next_agents.append(agent.reproduce())
            if agent.can_survive():
                next_agents.append(agent)

        self.distribute_resources()

    def distribute_resources(self):
        # TODO: implement
        pass
