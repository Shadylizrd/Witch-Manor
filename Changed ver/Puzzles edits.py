import random
from gpiozero import LED, Button
import time
from SimonSays import *
from KeyPuzzle import *

class Puzzles():
    def __init__(self):
        index=[]
        while len(index)<5:
            num=random.randint(0,4)
            if num not in index:
                index.append(num)
        
        self.__puzzles=[[SimonSays(3,index[0]),index[0]],[SimonSays(4,index[1]),index[1]]]
        self.__simonDifficulty=5
        for i in range(2,5):
            if random.randint(0,1)==0:
                self.__puzzles.append([KeyPuzzle(index[i], "puzzleRoom"),index[i]])
                self.__puzzles.append([KeyPuzzle(index[i], "keyRoom"),index[i]])
            else:
                self.__puzzles.append([SimonSays(self.__simonDifficulty,index[i]),index[i]])
                self.__simonDifficulty+=1

    def getPuzzles(self):
        return self.__puzzles