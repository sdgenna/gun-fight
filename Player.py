ACTIONS = ['shoot', 'laser', 'block', 'laserblock']


class Player:
    def __init__(self, name):
        self.name = name

    def act(self):
        return ACTIONS[0]
