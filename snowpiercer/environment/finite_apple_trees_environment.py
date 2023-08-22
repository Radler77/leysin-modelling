from snowpiercer.environment.environment import Environment
from snowpiercer.resources import Resource
from snowpiercer.resources.apple import Apple
from snowpiercer.resources.appletree import AppleTree


class FiniteAppleTreesEnvironment(Environment):

    trees: list[AppleTree] = []

    def __init__(self, initial_trees: int = 6):
        super().__init__(initial_resources=[])
        for i in range(initial_trees):
            self.trees.append(AppleTree())
            self.resources.append(self.trees[i])

    def remove_resource(self, resource: Resource):
        super().remove_resource(resource)
        if resource in self.trees:
            self.trees.remove(resource)

    def next_time_step(self):
        for tree in self.trees:
            for i in range(tree.get_apples_per_turn()):
                self.resources.append(Apple())
