import random
from gpiozero import LED, Button
import time
from SimonSays import *

PUZZLES=["SIMON", "KEY"]

class Puzzles():
    def __init__(self):
        #change to save objects
        self.__puzzles=[SimonSays(3),SimonSays(4)]
        self.__passedPuzzles=[False,False,False,False,False]
        self.__simonDifficulty=5
        for i in range(3):
            #makes a list of random colours the length of the difficulty
            if random.randint(0,1)==0:
                self.__puzzles.append("KEY")
            else:
                self.__puzzles.append(SimonSays(self.__simonDifficulty))
                self.__simonDifficulty+=1
        print(self.__puzzles)
           
           
    def simonSays(self):
        #checks if they got it correct
        passed=self.__puzzles[index].sequence()
        return passed
       
    #will call a key class
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
        complete=True
        for i in range(len(self.__puzzles)):
            if self.__passedPuzzles[i]==False:
                complete= False
        return complete

    #gets called when the player tries to complete a puzzle
    def runPuzzle(self, currentPuzzle):
        for i in range(len(self.__puzzles)):
            if self.__puzzles[i]==currentPuzzle:
                index=i     
            #checks which puzzle it is for
            if currentPuzzle.getType()=="SIMON":    
                if self.simonSays():
                    self.setPassedPuzzles(index)
            elif currentPuzzle.getType()=="KEY":    
                if self.key():
                    self.setPassedPuzzles(index)



puzzle=Puzzles()
#replace index with the a value obtained from the puzzle when it is found 
index=0

#example of how going through each of the puzzles could work
while puzzle.completedPuzzles()==False and index<5:
    #checks they haven't already completed that puzzle
    currentPuzzle=puzzle.getPuzzles()[index]
    for i in range(len(puzzle.getPuzzles())):
            if puzzle.getPuzzles()[i]==currentPuzzle:
                index=i
                if puzzle.checkCompleted(index)==False:
                    #checks which puzzle it is for
                    if currentPuzzle.getType()=="SIMON":    
                        correct=puzzle.simonSays(index)
                        if correct:
                            puzzle.setPassedPuzzles(index)
                    elif currentPuzzle.getType()=="KEY":    
                        correct=puzzle.key()
                        if correct:
                            puzzle.setPassedPuzzles(index)
                else:
                    print("You have already completed that puzzle \n")
    index+=1
