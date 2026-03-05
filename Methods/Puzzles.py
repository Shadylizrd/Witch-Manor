import random
from gpiozero import LED, Button
import time
from SimonSaysWithoutLEDs import *
PUZZLES=["SIMON", "CODE","KEY"]

class Puzzles():
    def __init__(self):
        self.__puzzles=[]
        self.__passedPuzzles=[False,False,False,False,False]
        self.__simonDifficulty=3
        for i in range(5):
            #makes a list of random colours the length of the difficulty
            self.__puzzles.append(PUZZLES[random.randint(0,2)])
            print(self.__puzzles)
            
            
    def simonSays(self):
        #checks if they got it correct
        passed=False
        while passed==False:
            #will create a new code each time even within the same puzzle if they get it wrong
            simon=SimonSays(self.__simonDifficulty)
            passed=simon.sequence()
        
        #the puzzle gets harder the more they do
        self.__simonDifficulty+=1
        return True
    
    #will call a code class?
    def code(self):
        return True
       
    #will call a key class?
    def key(self):
        return True
    
    #lists the types of puzzles to be put in the game
    def getPuzzles(self):
        return self.__puzzles
    
    #updates the passedPuzzLes list to true at the index for the puzzle passed
    def setPassedPuzzles(self, index):
        self.__passedPuzzles[index]=True
    
    #checks if all the puzzles have been passed
    def completedPuzzles(self):
        for i in range(5):
            if self.__passedPuzzles[i]==False:
                return False
        return True


puzzle=Puzzles()

#replace index with the a value obtained from the puzzle when it is found 
index=0

#example of how going through each of the puzzles could work
while puzzle.completedPuzzles()==False:
    if puzzle.getPuzzles()[index]=="SIMON":    
        puzzle.simonSays()
        puzzle.setPassedPuzzles(index)
        index+=1
    elif puzzle.getPuzzles()[index]=="CODE":    
        print(puzzle.code())
        puzzle.setPassedPuzzles(index)
        index+=1
    elif puzzle.getPuzzles()[index]=="KEY":    
        puzzle.key()
        puzzle.setPassedPuzzles(index)
        index+=1
