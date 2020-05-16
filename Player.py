import random
ACTIONS = ['load', 'shoot', 'laser', 'block', 'laserblock']
DEBUG = 'True'

class Player:
    def __init__(self, name):
        self.name = name
        self.player_memory = []
        self.opponent_memory = []

    def act(self, player_action_id):
        player_action = ACTIONS[player_action_id]
        if DEBUG:
            print(self.name + " has launched : " + player_action)
        return player_action

    def random_act(self):
        player_action = random.choice(ACTIONS)
        if DEBUG:
            print(self.name + " has launched :  " + player_action)
        return player_action

    def read(self,opponent_action):
        # Convert string into integer
        switcher  = {
            "load": 0,
            "shoot": 1,
            "laser": 2,
            "block": 3,
            "laserblock": 4,
        }

        return switcher.get(opponent_action,"Action Not Understood")

    def memorize_opponent_action(self, opponent_action_id):
        self.opponent_memory.append(opponent_action_id)
        if DEBUG:
            print(self.name+" has remembered the opponent action : " + ACTIONS[opponent_action_id])

    def memorize_player_action(self, my_action_id):
        self.player_memory.append(my_action_id)
        if DEBUG:
            print(self.name+ " has remembered its own action : " + ACTIONS[my_action_id])

