import random
from gpiozero import LED, Button
import time
from SimonSays import *
from codePuzzle import *

class Puzzles():
    def __init__(self):
        self.__puzzles=["SIMON","SIMON",]
        self.__passedPuzzles=[False,False,False,False,False]
        self.__simonDifficulty=3
        for i in range(3):
            #makes a list of random colours the length of the difficulty
            self.__puzzles.append(PUZZLES[random.randint(0,1)])
            print(self.__puzzles)
            
    def simonSays(self):
        #checks if they got it correct
        passed=False
        broke=False
        while passed==False and broke==False:
            #while in the puzzle state the interact key, if pressed will set broke to True
            #will create a new code each time even within the same puzzle if they get it wrong
            simon=SimonSays(self.__simonDifficulty)
            passed, broke=simon.sequence()
        
        #the puzzle gets harder the more they do
        self.__simonDifficulty+=1
        return passed
       
    #will call a key class?
    def key(self):
        return True
    
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
        for i in range(5):
            if self.__passedPuzzles[i]==False:
                return False
        return True

    #gets called when the player tries to complete a puzzle
    def runPuzzle(self, currentPuzzle):
        for i in range(len(self.__puzzles)):
            if self.__puzzles[i]==currentPuzzle:
                index=i
        if puzzle.checkCompleted(index)==False:      
            #checks which puzzle it is for
            if currentPuzzle.getType()=="SIMON":    
                if puzzle.simonSays():
                    puzzle.setPassedPuzzles(index)
            elif currentPuzzle.getType()=="KEY":    
                if puzzle.key():
                    puzzle.setPassedPuzzles(index)
        else:
            print("You have already completed that puzzle \n")

puzzle=Puzzles()

#replace index with the a value obtained from the puzzle when it is found 
index=0

#example of how going through each of the puzzles could work
while puzzle.completedPuzzles()==False and index<5:
    #checks they haven't already completed that puzzle
    if puzzle.checkCompleted(index)==False:
        
        #checks which puzzle it is for
        if puzzle.getPuzzles()[index]=="SIMON":    
            if puzzle.simonSays():
                puzzle.setPassedPuzzles(index)
        elif puzzle.getPuzzles()[index]=="KEY":    
            if puzzle.key():
                puzzle.setPassedPuzzles(index)
    else:
        print("You have already completed that puzzle \n")

