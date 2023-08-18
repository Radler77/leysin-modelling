from abc import ABC, abstractmethod

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
    def placeholder_method(self):
            pass
    
    @abstractmethod
    def handle_conflict(Agent : self, ):
        pass