# 1. 1 Player  Name Added
# 1. 2 Player Memory Added
# 1. 3 Player Internal Rule will be added (In Progress)


import random
ACTIONS = ['shoot', 'laser', 'block', 'laserblock', 'load']
DEBUG = 'False'

class Player:
    def __init__(self, name):
        self.name = name
        self.player_memory = []
        self.opponent_memory = []

    def deterministic_act(self, player_action_id):
        player_action = ACTIONS[player_action_id]
        if DEBUG:
            print(self.name + " has launched : " + player_action)
        return player_action

    def act(self):
        player_action = random.choice(ACTIONS)
        if DEBUG:
            print(self.name + " has launched :  " + player_action)
        return player_action

    def read(self,opponent_action):
        # Convert string into integer
        switcher  = {
            "shoot": 0,
            "laser": 1,
            "block": 2,
            "laserblock": 3,
            "load": 4,
        }

        return switcher.get(opponent_action,"Action Not Understood")

    def memorize_opponent_action(self, opponent_action_id):
        self.opponent_memory.append(opponent_action_id)
        if DEBUG:
            print(self.name+" has remembered the opponent action : " + ACTIONS[opponent_action_id])
            print(self.name + " remembered " + str(self.opponent_memory) + " as the opponent actions")


    def memorize_own_action(self, my_action_id):
        self.player_memory.append(my_action_id)
        if DEBUG:
            print(self.name+ " has remembered its own action : " + ACTIONS[my_action_id])
            print(self.name + " remembered " + str(self.player_memory) + " as its own actions")




