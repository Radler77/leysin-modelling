import numpy as np
import matplotlib.pyplot as plt


class PopulationPlotter:

    def plot(self, population_size_log):
        plt.plot(population_size_log)
        plt.title("Population Size Log")
        plt.xlabel("Time")
        plt.ylabel("Population Size (log scale)")
        plt.grid(True)
        plt.show()
