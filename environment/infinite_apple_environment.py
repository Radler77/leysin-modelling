from environment.environment import Environment
from environment.resources.apple import Apple


class InfiniteAppleEnvironment(Environment):
    new_apples_per_timestep = 10

    def next_time_step(self):
        for i in range(self.new_apples_per_timestep):
            self.resources.append(Apple())
