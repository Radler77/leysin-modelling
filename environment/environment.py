from environment.resources.resource import Resource
from abc import ABC, abstractmethod


class Environment(ABC):
    resources: [Resource] = []

    def __init__(self, initial_resources: [Resource]):
        self.resources = initial_resources

    def get_resources(self):
        return self.resources

    @abstractmethod
    def next_time_step(self):
        pass
