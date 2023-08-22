from snowpiercer.resources.appletree import AppleTree
from snowpiercer.resources.resource import Resource
from abc import ABC, abstractmethod


class Environment(ABC):
    resources: [Resource] = []

    def __init__(self, initial_resources: [Resource]):
        self.resources = initial_resources

    def add_resource(self, resource: Resource):
        self.resources.append(resource)

    def remove_resource(self, resource: Resource):
        self.resources.remove(resource)

    @abstractmethod
    def next_time_step(self):
        pass
