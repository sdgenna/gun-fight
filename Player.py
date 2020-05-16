import random

ACTIONS = ['shoot', 'laser', 'block', 'laserblock', 'load']


class Player:
    def __init__(self, name):
        self.name = name

    def act(self):
        random.choice(ACTIONS)
