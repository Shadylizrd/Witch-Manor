import random
from gpiozero import LED, Button
import time
#takes a difficulty which is how many colours will be in the sequence

COLOURS=["RED", "BLUE", "GREEN", "YELLOW"]
class SimonSays():
    
    def __init__(self,difficulty):
        
        #setting up the I/O
        #LEDs
        self.__red=LED(21)
        self.__green=LED(20)
        self.__blue=LED(16)
        self.__yellow=LED(12)
        #Buttons
        self.__redButton=Button(23)
        self.__greenButton=Button(22)
        self.__blueButton=Button(27)
        self.__yellowButton=Button(17)
        self.__exitButton=Button(4)         
        
        #setting up variables
        self.__answer=[]
        self.__type= "SIMON"
        
        #put the difficulty in the Puzzles class
        self._difficulty=difficulty
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
    
    #checks if the user has entered the entire sequence correctly
    #recoursively calls itself until the entire sequence is done
    def sequence(self):
        self.__currentDifficulty+=1
        #runs the number of times that the difficulty is 1 to difficulty
        self.showSequence()
        correct, toBreak=self.checkSequence()
        if correct:
            if self._difficulty==self.__currentDifficulty:
                #returns true if the game has been won
                return True
            else:
                passed=self.sequence()
                return passed
        elif toBreak==True:
            return False
        else:
            self.newAnswer()
            passed=self.sequence()
            return passed
            
            
    #flashes the sequence for the player to copy
    def showSequence(self):
        for i in range(self.__currentDifficulty):
            if self.__answer[i]=="RED":
                self.__red.on()
            elif self.__answer[i]=="BLUE":
                self.__blue.on()
            elif self.__answer[i]=="GREEN":
                self.__green.on()
            elif self.__answer[i]=="YELLOW":
                self.__yellow.on()
            time.sleep(0)
            #makes sure all LEDs are off before showing the next LED
            self.__red.off()
            self.__green.off()
            self.__blue.off()
            self.__yellow.off()


    #checks the user input against the sequence returns False if it isn't the same
    def checkSequence(self):
        toBreak=False
        correct=True
        #loops for each LED in sequence
        for i in range(self.__currentDifficulty):
            pressed=False
            #will loop until a button is pressed
            while pressed==False:
                
                #checks if each button is pressed then if that was the button that was supposed to be pressed
                if self.__redButton.is_pressed:
                    pressed=True
                    if self.__answer[i]!="RED":
                        #returns False if it was not the correct button
                        return False, toBreak
                    
                elif self.__blueButton.is_pressed:
                    pressed=True
                    if self.__answer[i]!="BLUE":
                        return False, toBreak
                    
                elif self.___greenButton.is_pressed:
                    pressed=True
                    if self.__answer[i]!="GREEN":
                        return False, toBreak
                    
                elif self.__yellowButton.is_pressed:
                    pressed=True
                    if self.__answer[i]!="YELLOW":
                        return False, toBreak
                    
                elif self.__exitButton.is_pressed:
                    return False, True
                    
                    
        return correct, toBreak
                
        
        