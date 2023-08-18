from simulation.population_plotter import PopulationPlotter
from simulation.simulation import Simulation

# main
if __name__ == '__main__':
    simulation: Simulation = Simulation(number_of_timesteps=100)
    simulation.run()
    PopulationPlotter().plot((simulation.get_population_size_log()))
