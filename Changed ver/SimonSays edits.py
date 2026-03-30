import random
from gpiozero import LED, Button
import time
from ReadJson import *
from Config import BUTTONS

COLOURS=["RED", "BLUE", "GREEN", "YELLOW"]
BUTTON_MAP = {0: "RED", 1: "BLUE", 2: "GREEN", 3: "YELLOW"}

class SimonSays():
    
    def __init__(self,difficulty, puzzleIndex):
        self.__simonDict = readJson('SimonDescriptions.json', 'SimonRoomDescriptions')[puzzleIndex]
        self.__puzzleDescription = self.__simonDict['puzzleDescription']
        self.__solvedDescription = self.__simonDict['solvedDescription']
        self.__answer=[]
        self.__type= "SIMON"
        
        self.__difficulty=difficulty
        self.__currentDifficulty=0
        for i in range(difficulty):
            self.__answer.append(COLOURS[random.randint(0,3)])
    
    def getType(self):
        return self.__type
    
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
        
    def sequence(self, gameState):
        self.__currentDifficulty+=1
        self.showSequence()
        correct, toBreak = self.checkSequence(gameState)
        if correct:
            if self.__difficulty==self.__currentDifficulty:
                return True
            else:
                return self.sequence(gameState)
        elif toBreak==True:
            return False
        else:
            self.newAnswer()
            return self.sequence(gameState)
            
    def showSequence(self):
        for i in range(self.__currentDifficulty):
            if self.__answer[i]=="RED": BUTTONS.led1()
            elif self.__answer[i]=="BLUE": BUTTONS.led2()
            elif self.__answer[i]=="GREEN": BUTTONS.led3()
            elif self.__answer[i]=="YELLOW": BUTTONS.led4()

    def checkSequence(self, gameState):
        toBreak=False
        correct=True
        for i in range(self.__currentDifficulty):
            pressed=False
            while pressed==False:
                gameState.tick() 
                userInput = BUTTONS.getInput()
                
                # Check mapping instead of hardcoded numbers
                if userInput in BUTTON_MAP:
                    pressed = True
                    if self.__answer[i] != BUTTON_MAP[userInput]:
                        return False, toBreak
                elif userInput == 4:
                    return False, True
                    
        return correct, toBreak