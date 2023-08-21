import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt


class PopulationPlotter:

    def plot(self, population_size_log : npt.NDArray['int']):
        plt.plot(population_size_log)
        plt.title("Population Size")
        plt.xlabel("Time")
        plt.ylabel("Individuals")
        plt.grid(True)
        plt.show()
