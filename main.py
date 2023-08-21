from snowpiercer.simulation import PopulationPlotter
from snowpiercer.simulation import Simulation

# main script
if __name__ == '__main__':
    simulation: Simulation = Simulation(number_of_timesteps=100)
    simulation.run()
    PopulationPlotter().plot((simulation.get_population_size_log()))
