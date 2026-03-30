import random
from gpiozero import LED, Button
import time
from SimonSays import *
from KeyPuzzle import *

PUZZLES=["SIMON", "KEY"]

class Puzzles():
    def __init__(self):
        #generates an array of 5 different unique index
        index=[]
        while len(index)<5:
            num=random.randint(0,4)
            if num not in index:
                index.append(num)
        
        self.__puzzles=[[SimonSays(3,index[0]),index[0]],[SimonSays(4,index[1]),index[1]]]
        self.__passedPuzzles=[False,False,False,False,False]
        self.__simonDifficulty=5
        for i in range(2,5):
            #makes a list of random colours the length of the difficulty
            if random.randint(0,1)==0:
                self.__puzzles.append([KeyPuzzle(index[i], "puzzleRoom"),index[i]])
                self.__puzzles.append([KeyPuzzle(index[i], "keyRoom"),index[i]])
            else:
                self.__puzzles.append([SimonSays(self.__simonDifficulty,index[i]),index[i]])
                self.__simonDifficulty+=1

    
    #lists the types of puzzles to be put in the game
    def getPuzzles(self):
        return self.__puzzles
    
    #updates the passedPuzzLes list to true at the index for the puzzle passed
    def setPassedPuzzles(self, index):
        self.__passedPuzzles[index]=True
    
    def checkCompleted(self,index):
        return self.__passedPuzzles[index]
        
    #checks if all the puzzles have been passed
    def completedPuzzles(self):
        complete=True
        for i in range(len(self.__puzzles)):
            if self.__passedPuzzles[i]==False:
                complete= False
        return complete

