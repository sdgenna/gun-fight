import random

ACTIONS = ['shoot', 'laser', 'block', 'laserblock', 'load']


class Player:
    def __init__(self, name):
        self.name = name

    def random_act(self):
        random.choice(ACTIONS)
        
    def action(self,action_id):
        switch(action_id):
            
            case 1: Do shoot
            case 2: Do laser    
                ....
                
                
