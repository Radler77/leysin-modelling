import numpy as np
import numpy.typing as npt

from snowpiercer.world.world import World


class Simulation:
    number_of_timesteps: int = None

    world: World = None
    population_size_log : npt.NDArray['int'] = None

    def __init__(self, number_of_timesteps: int):
        self.number_of_timesteps = number_of_timesteps
        self.world = World.create_simple_world()
        self.population_size_log = np.empty(self.number_of_timesteps, dtype='int')

    def run(self):
        for i in range(self.number_of_timesteps):
            population_size: int = self.world.get_population_size()
            self.population_size_log[i] = population_size
            self.world.next_time_step()

    def get_population_size_log(self):
        return self.population_size_log
