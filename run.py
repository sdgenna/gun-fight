NUM_ROUNDS = 10
import Player
import Tristan
import Sylvain

tristan = Tristan()
sylvain = Sylvain()
tristanAmmo = 0
sylvainAmmo = 0

for round in range(NUM_ROUNDS):
    print("Round number {0}".format(round + 1))
    tristanAction = tristan.act()
    sylvainAction = sylvain.act()
    if tristanAction == Player.ACTIONS[-1]:
        tristanAmmo += 1
    if sylvainAction == Player.ACTIONS[-1]:
        sylvainAmmo += 1
