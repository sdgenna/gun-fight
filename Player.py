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
            print(self.name + " has " + player_action)
        return player_action

    def random_act(self):
        player_action = random.choice(ACTIONS)
        if DEBUG:
            print(self.name + " has " + player_action)
        return player_action
