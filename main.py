from snowpiercer.simulation import PopulationPlotter
from snowpiercer.simulation import Simulation
from snowpiercer.world import World

import matplotlib.pyplot as plt

# main script
if __name__ == '__main__':
    simulation: Simulation = Simulation(number_of_timesteps=100, world=World.create_simple_conflict_avoidant_world())
    simulation.run()
    PopulationPlotter().plot(simulation.get_data_log())
