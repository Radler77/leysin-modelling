import numpy as np
from world import World
from world.world import create_simple_world


class Simulation:
    number_of_timesteps: int = None

    world: World = None
    population_size_log = None

    def __init__(self, number_of_timesteps: int):
        self.number_of_timesteps = number_of_timesteps
        self.world = create_simple_world()
        population_size_log = np.empty(self.number_of_timesteps)

    def run(self):
        for i in range(self.number_of_timesteps):
            population_size: int = self.world.get_population_size()
            self.population_size_log[i] = population_size
            self.world.next_time_step()

    def get_population_size_log(self):
        return self.population_size_log
