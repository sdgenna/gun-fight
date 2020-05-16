import Player
import Tristan
import Sylvain
from datetime import datetime
import time
import logging
from sys import stdout

NUM_ROUNDS = 10
NUM_TURNS_PER_ROUND = 10


def writeLog(message, logObject):
    timestamp = datetime.now()
    logObject.info("[{0}]: {1}".format(str(timestamp), message))
    return


def runOneRound(Player1, Player2):
    Player1Ammo = 0
    Player2Ammo = 0

    for turnNumber in range(NUM_TURNS_PER_ROUND):
        writeLog("Turn number {0}".format(turnNumber + 1), logger)


        Player1Action = Player1.act()
        Player2Action = Player2.act()

        NAME = [Player1, Player2]
        Player1Action_ID = NAME[0].read(Player1Action)
        Player2Action_ID = NAME[1].read(Player2Action)
        NAME[0].memorize_own_action(Player1Action_ID)
        NAME[0].memorize_opponent_action(Player2Action_ID)
        NAME[1].memorize_own_action(Player2Action_ID)
        NAME[1].memorize_opponent_action(Player1Action_ID)


        if Player1Action == Player.ACTIONS[-1]:
            Player1Ammo += 1
        if Player2Action == Player.ACTIONS[-1]:
            Player2Ammo += 1

        if Player1Action == Player.ACTIONS[0]:
            if Player1Ammo <= 0:
                writeLog("{0} loses".format(Player1.name), logger)
                break
            else:
                Player1Ammo -= 1
                if Player2Action != Player.ACTIONS[2] or Player2Action != Player.ACTIONS[0] or Player2Action != Player.ACTIONS[1]:
                    writeLog("{0} loses".format(Player2.name), logger)
                    break

        elif Player1Action == Player.ACTIONS[1]:
            if Player1Ammo <= 1:
                writeLog("{0} loses".format(Player1.name), logger)
                break
            else:
                Player1Ammo -= 2
                if Player2Action != Player.ACTIONS[3] or Player2Action != Player.ACTIONS[1]:
                    writeLog("{0} loses".format(Player2.name), logger)
                    break

        if Player2Action == Player.ACTIONS[0]:
            if Player2Ammo <= 0:
                writeLog("{0} loses".format(Player2.name), logger)
                break
            else:
                Player2Ammo -= 1
                if Player1Action != Player.ACTIONS[2] or Player1Action != Player.ACTIONS[0] or Player1Action != Player.ACTIONS[1]:
                    writeLog("{0} loses".format(Player1.name), logger)
                    break
        elif Player2Action == Player.ACTIONS[1]:
            if Player2Ammo <= 1:
                writeLog("{0} loses".format(Player2.name), logger)
                break
            else:
                Player2Ammo -= 2
                if Player1Action != Player.ACTIONS[3] or Player1Action != Player.ACTIONS[1]:
                    writeLog("{0} loses".format(Player1.name), logger)
                    break


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, stream=stdout)
logger.addHandler(logging.FileHandler("logTournament.txt"))
writeLog("Running tournament", logger)

tristan = Tristan.Tristan()
sylvain = Sylvain.Sylvain()

runOneRound(tristan, sylvain)
