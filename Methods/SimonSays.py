import random
from gpiozero import LED, Button
import time
from GameState import *
from ReadJson import *
from MovementControls import *
#takes a difficulty which is how many colours will be in the sequence

COLOURS=["RED", "BLUE", "GREEN", "YELLOW"]
class SimonSays():
    
    def __init__(self,difficulty, puzzleIndex):
                
        self.__simonDict = readJson('SimonDescriptions.json', 'SimonRoomDescriptions')[puzzleIndex]
        self.__puzzleDescription = self.__simonDict['puzzleDescription']
        self.__solvedDescription = self.__simonDict['solvedDescription']
        
        #setting up variables
        self.__answer=[]
        self.__type= "SIMON"
        
        #put the difficulty in the Puzzles class
        self.__difficulty=difficulty
        self.__currentDifficulty=0
        for i in range(difficulty):
            #makes a list of random colours the length of the difficulty
            self.__answer.append(COLOURS[random.randint(0,3)])
    
    #returns the puzzle type
    def getType(self):
        return self.__type
    
    #regenerates sequence when the player gets it wrong
    def newAnswer(self):
        self.__answer=[]
        self.__currentDifficulty=0
        for i in range(self.__difficulty):
            self.__answer.append(COLOURS[random.randint(0,3)])

    def solvedDescription(self):
        print(self.__solvedDescription)
        print("")

    def enterRoom(self, gameState):
        print(self.__puzzleDescription)
        print("")
        return self.sequence(gameState)
        
    #checks if the user has entered the entire sequence correctly
    #recoursively calls itself until the entire sequence is done
    def sequence(self, gameState):
        self.__currentDifficulty+=1
        #runs the number of times that the difficulty is 1 to difficulty
        self.showSequence()
        correct, toBreak = self.checkSequence(gameState)
        if correct:
            if self.__difficulty==self.__currentDifficulty:
                #returns true if the game has been won
                return True
            else:
                passed = self.sequence(gameState)
                return passed
        elif toBreak==True:
            return False
        else:
            self.newAnswer()
            passed = self.sequence(gameState)
            return passed
            
            
    #flashes the sequence for the player to copy
    def showSequence(self):
        for i in range(self.__currentDifficulty):
            if self.__answer[i]=="RED":
                MovementControls.led1()
            elif self.__answer[i]=="BLUE":
                MovementControls.led2()
            elif self.__answer[i]=="GREEN":
                MovementControls.led3()
            elif self.__answer[i]=="YELLOW":
                MovementControls.led4()


    #checks the user input against the sequence returns False if it isn't the same
    def checkSequence(self, gameState):
        toBreak=False
        correct=True
        #loops for each LED in sequence
        for i in range(self.__currentDifficulty):
            pressed=False
            #will loop until a button is pressed
            while pressed==False:
                
                # Updates the main game timer and LED flashing while the puzzle is running
                # This prevents the timer from freezing when inside a puzzle loop
                gameState.tick() 
                
                #checks if each button is pressed then if that was the button that was supposed to be pressed
                if BUTTONS.getInput()==0:
                    pressed=True
                    if self.__answer[i]!="RED":
                        #returns False if it was not the correct button
                        return False, toBreak
                    
                elif BUTTONS.getInput()==1:
                    pressed=True
                    if self.__answer[i]!="BLUE":
                        return False, toBreak
                    
                elif BUTTONS.getInput()==2:
                    pressed=True
                    if self.__answer[i]!="GREEN":
                        return False, toBreak
                    
                elif BUTTONS.getInput()==3:
                    pressed=True
                    if self.__answer[i]!="YELLOW":
                        return False, toBreak
                    
                elif BUTTONS.getInput()==4:
                    return False, True
                    
                    
        return correct, toBreak
                
        
        