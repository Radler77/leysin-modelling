from __future__ import annotations
from typing import List

from snowpiercer.environment.environment import Environment
from snowpiercer.agents.agent import Agent
from snowpiercer.resources.resource import Resource
from snowpiercer.conflicts.conflict import Conflict
from snowpiercer.conflicts.conflict_resolver import ConflictResolver


class World:
    environment: Environment = None
    agents: List[Agent] = []
    resolve_strategy: ConflictResolver = None

    def __init__(self, resolve_strategy: ConflictResolver, environment: Environment, agents: List[Agent]):
        self.resolve_strategy = resolve_strategy
        self.environment = environment
        self.agents = agents

    def get_population_size(self):
        return len(self.agents)

    def next_time_step(self):
        """Executes one time step in this world. This includes updating the environment and available resources,
        updating the population and distributing resources to the agents."""
        self.environment.next_time_step()
        self.update_population()
        self.distribute_resources()

    def update_population(self):
        """Updates the population of this world. This includes reproduction and death of agents."""
        next_agents: List[Agent] = []
        for agent in self.agents:
            agent.next_timestep()
            if agent.can_reproduce():
                next_agents.append(agent.reproduce())
            if agent.can_survive():
                next_agents.append(agent)
        self.agents = next_agents

    def distribute_resources(self):
        """Distributes resources to the agents. This includes agents choosing which resources they desire, allowing them
        to change their minds if another agent wants the same resource, and handling remaining conflicts after all agents
        have settled on their decision."""
        agent_conflicts, conflicts = self.create_initial_conflicts()
        # TODO: allow agents to change their mind multiple times
        self.allow_agents_to_change_mind(agent_conflicts)
        rewards = self.resolve_remaining_conflicts(conflicts)

        for agent in rewards.keys():
            rewards[agent].consumed_by(agent)
            self.environment.resources.remove(rewards[agent])

    def resolve_remaining_conflicts(self, conflicts):
        """Resolves the remaining conflicts after all agents have settled on their decision. For example, if two agents
        want the same resource, but only one can have it, we might punish both agents since they are now fighting for the
        same resource."""
        rewards: dict[Agent, Resource] = self.resolve_strategy.resolve_conflict(list(conflicts.values()))
        return rewards

    def allow_agents_to_change_mind(self, agent_conflicts):
        for agent in agent_conflicts.keys():
            agent.handle_conflict(agent_conflicts[agent])

    def create_initial_conflicts(self):
        conflicts: dict[Resource, Conflict] = {}
        agent_conflicts: dict[Agent, Conflict] = {}
        for agent in self.agents:
            preferred_resource: Resource = agent.initial_resource_selection(self.environment.resources)
            if preferred_resource not in conflicts.keys():
                conflicts[preferred_resource] = Conflict(contested_ressource=preferred_resource,
                                                         agents_involved=[agent])
            else:
                conflicts[preferred_resource].add_agent_involved(agent)

            agent_conflicts[agent] = conflicts[preferred_resource]
        return agent_conflicts, conflicts

    @staticmethod
    def create_simple_world() -> World:
        from snowpiercer.conflicts import PrisonerDilemmaResolver
        from snowpiercer.environment import InfiniteAppleEnvironment
        from snowpiercer.agents import NormieAgent

        resolve_strategy = PrisonerDilemmaResolver()
        environment = InfiniteAppleEnvironment(30)
        agents = []
        for i in range(0, 30):
            agents.append(NormieAgent())
        return World(resolve_strategy=resolve_strategy, environment=environment, agents=agents)
