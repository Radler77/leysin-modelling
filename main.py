import time

from snowpiercer.simulation import PopulationPlotter
from snowpiercer.simulation import Simulation
from snowpiercer.world import World

# main script
if __name__ == '__main__':
    simulation: Simulation = Simulation(number_of_timesteps=200, world=World.create_simple_mixed_world())
    simulation.run()
    PopulationPlotter().plot(simulation.get_data_log())
