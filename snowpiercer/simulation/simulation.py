import numpy as np
import numpy.typing as npt
import pandas as pd

from snowpiercer.world.world import World


class Simulation:
    number_of_timesteps: int = None
    world: World = None    
    data: pd.DataFrame = None
    
    def __init__(self, number_of_timesteps: int, world: World):
        self.number_of_timesteps = number_of_timesteps
        self.world = world
        self.data = pd.DataFrame(columns=['time', 'population_size', 'born', 'died'])
        
    def run(self, trackAggressiveAgents: bool = False):
        self.data = self.run_experiment(trackAggressiveAgents=trackAggressiveAgents)

    def run_experiment(self, trackAggressiveAgents: bool = False) -> pd.DataFrame:
        if trackAggressiveAgents:
            data = {'time': np.zeros(self.number_of_timesteps), 'population_size': np.zeros(self.number_of_timesteps), 'born': np.zeros(self.number_of_timesteps), 'died': np.zeros(self.number_of_timesteps), 'aggressiveAgents': np.zeros(self.number_of_timesteps)}
        else:
            data = {'time': np.zeros(self.number_of_timesteps), 'population_size': np.zeros(self.number_of_timesteps), 'born': np.zeros(self.number_of_timesteps), 'died': np.zeros(self.number_of_timesteps)}
        
        for i in range(self.number_of_timesteps):
            population_size: int = self.world.get_population_size()
            born: int = self.world.get_born_count()
            died: int = self.world.get_died_count()
            
            data['time'][i] = i
            data['population_size'][i] = population_size
            data['born'][i] = born
            data['died'][i] = died
            
            if trackAggressiveAgents:
                data['aggressiveAgents'][i] = self.world.get_num_aggressive_agents()
            
            self.world.next_time_step()

        df = pd.DataFrame.from_dict(data)
        return df

    def get_data_log(self) -> pd.DataFrame:
        return self.data
