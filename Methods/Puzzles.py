import random
#from gpiozero import LED, Button
import time
from SimonSaysWithoutLEDs import *
PUZZLES=["SIMON", "CODE"]
class Puzzles():
    def __init__(self):
        self.__puzzles=[]
        self.__simonDifficulty=3
        for i in range(5):
            #makes a list of random colours the length of the difficulty
            self.__puzzles.append(PUZZLES[random.randint(0,1)])
    def simonSays(self):
        passed=False
        while passed==False:
            passed=SimonSaysWithoutLEDs(self.__simonDifficulty)
            
        simonDifficulty+=1
        return "Done"
puzzle=Puzzles()
print(puzzle.simonSays())