from agents import Agent
from environment.resources import Resource
from .conflict import Conflict
from .conflict_resolver import ConflictResolver


class PrisonerDilemmaResolver(ConflictResolver):

    def resolve_conflict(self, conflicts: list[Conflict]) -> dict[Agent, Resource]:
        rewards: dict[Agent, Resource] = {}

        for conflict in conflicts:
            if len(conflict.agents_involved) == 1:
                rewards[conflict.agents_involved[0]] = conflict.contested_ressource
            # if there are multiple agents involved, noone gets the resource and all agents get a punishment
            else:
                for agent in conflict.agents_involved:
                    agent.change_satiety(-0.2)

        return rewards