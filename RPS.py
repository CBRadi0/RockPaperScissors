import random, os, time
from RPSImport import RPS
clear = lambda: os.system('cls')
while True:
    clear()
    Game = RPS()

    Game.setUp()
    clear()
    Game.processChoice()
    Game.play()
    time.sleep(2)
    clear()