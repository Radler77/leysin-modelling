from abc import ABC, abstractmethod
from typing import List, Optional

from conflicts.conflict import Conflict
from environment.resources import Resource

class Agent(ABC):
    
    reproduction_rate = .0
    
    satiety = .0
    
    # minimum basic_need_fulfillment that an Agent needs to survive
    survival_threshold = .3
    
    money_balance = 0
    
    # how likely the agent is to give up in a conflict / for a contested ressource
    conflict_aversion = .0
    
    # how likely the agent is to give up on updating its decision when getting new information / in a new decision round
    decision_fatigue = .0

        
    def get_basic_need_fulfillment(self):
        #TODO: implement more complex metric
        return self.satiety

    def eat(self, amount: float):
        self.satiety = max(1, self.satiety + amount)
    
    @abstractmethod
    def initial_resource_selection(self, resources : List[Resource]) ->  Optional[Resource]:
        pass
    
    @abstractmethod
    def handle_conflict(self, conflict : Conflict):
        pass