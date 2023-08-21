from environment.environment import Environment
from environment.resources.apple import Apple


class InfiniteAppleEnvironment(Environment):
    new_apples_per_timestep: int = None

    def __init__(self, new_apples_per_timestep: int = 10):
        self.new_apples_per_timestep = new_apples_per_timestep
        super().__init__(initial_resources=[])

    def next_time_step(self):
        for i in range(self.new_apples_per_timestep):
            self.resources.append(Apple())
