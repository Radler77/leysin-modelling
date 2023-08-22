import numpy as np
import numpy.typing as npt
import pandas as pd
import matplotlib.pyplot as plt


class PopulationPlotter:
    
    def plot(self, df: pd.DataFrame, title: str = None, population_size: bool = True, born: bool = True, died: bool = True, population_composition: bool = False):
        if title is not None:
            plt.title(title)
            
        plt.xlabel('Time')
        plt.ylabel('Number of individuals')
        
        if population_size:
            plt.plot(df['time'], df['population_size'], label='Population size')
        if born:
            plt.plot(df['time'], df['born'], label='Born rate')
        if died:
            plt.plot(df['time'], df['died'], label='Died rate')
        if population_composition:
            #TODO generalise this to multiple types of agents
            plt.plot(df['time'], df['aggressiveAgents'], label='Aggressive agents')
        
        plt.legend()
        plt.show()

    def plot_wood_resources(self, df: pd.DataFrame):
        plt.xlabel('Time')
        plt.ylabel('Number of wood resources')

        plt.plot(df['time'], df['wood resources'], label='Wood resources')

        plt.legend()
        plt.show()
