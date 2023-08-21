from typing import List

from conflicts.conflict import Conflict
from environment import Environment
from agents import Agent
from environment.resources import Resource
from conflicts import ConflictResolver


class World:
    environment: Environment = None
    agents: List[Agent] = []
    resolve_strategy: ConflictResolver = None
    resources: List[Resource] = []

    def __init__(self, resolve_strategy: ConflictResolver, environment: Environment, agents: List[Agent]):
        self.resolve_strategy = resolve_strategy
        self.environment = environment
        self.agents = agents

    def get_population_size(self):
        return len(self.agents)

    def next_time_step(self):
        self.environment.next_time_step()
        self.update_population()
        self.distribute_resources()

    def update_population(self):
        next_agents: List[Agent] = []
        for agent in self.agents:
            if agent.can_reproduce():
                next_agents.append(agent.reproduce())
            if agent.can_survive():
                next_agents.append(agent)
        self.agents = next_agents

    def distribute_resources(self):
        agent_conflicts, conflicts = self.create_initial_conflicts()
        # TODO: allow agents to change their mind multiple times
        self.allow_agents_to_change_mind(agent_conflicts)
        rewards = self.resolve_remaining_conflicts(conflicts)

        for agent in rewards.keys():
            rewards[agent].consumed_by(agent)

    def resolve_remaining_conflicts(self, conflicts):
        rewards: dict[Agent, Resource] = self.resolve_strategy.resolve_conflict(list(conflicts.values()))
        return rewards

    def allow_agents_to_change_mind(self, agent_conflicts):
        for agent in agent_conflicts.keys():
            agent.handle_conflict(agent_conflicts[agent])

    def create_initial_conflicts(self):
        conflicts: dict[Resource, Conflict] = {}
        agent_conflicts: dict[Agent, Conflict] = {}
        for agent in self.agents:
            preferred_resource: Resource = agent.initial_resource_selection(self.resources)
            if preferred_resource not in conflicts.keys():
                conflicts[preferred_resource] = Conflict(contested_ressource=preferred_resource,
                                                         agents_involved=[agent])
            else:
                conflicts[preferred_resource].add_agent_involved(agent)

            agent_conflicts[agent] = conflicts[preferred_resource]
        return agent_conflicts, conflicts


def create_simple_world() -> World:
    from conflicts import PrisonerDilemmaResolver
    from environment import InfiniteAppleEnvironment
    from agents import NormieAgent

    resolve_strategy = PrisonerDilemmaResolver()
    environment = InfiniteAppleEnvironment(30)
    agents = []
    for i in range(0, 30):
        agents.append(NormieAgent())
    return World(resolve_strategy=resolve_strategy, environment=environment, agents=agents)
