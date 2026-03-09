import random
from gpiozero import LED, Button
import time
#takes a difficulty which is how many colours will be in the sequence

COLOURS=["RED", "BLUE", "GREEN", "YELLOW"]
class SimonSays():
    
    def __init__(self,difficulty):
        
        self.__type= "SIMON"
        #setting up the I/O
        
        #LEDs
        self.__red="red"
        self.__green="green"
        self.__blue="blue"
        self.__yellow="yellow"
        #Buttons
        self.__redButton=Button(23)
        self.__greenButton=Button(22)
        self.__blueButton=Button(27)
        self.__yellowButton=Button(17)
        self.__exitButton=Button(4)
         
        
        #setting up variables
        self.__answer=[]
        
        #put the difficulty in the Puzzles class
        self._difficulty=difficulty
        self.__currentDifficulty=0
        for i in range(difficulty):
            #makes a list of random colours the length of the difficulty
            self.__answer.append(COLOURS[random.randint(0,3)])
    
    #returns the puzzle type
    def getType(self):
        return self.__type
    
    #checks if the user has entered the entire sequence correctly
    #recoursively calls itself until the entire sequence is done
    def sequence(self):
        self.__currentDifficulty+=1
        #runs the number of times that the difficulty is 1 to difficulty
        self.showSequence()
        correct, broke=self.checkSequence()
        if correct:
            if self._difficulty==self.__currentDifficulty:
                #returns true if the game has been won
                return True, False
            else:
                passed=self.sequence()
                return passed
        elif broke==True:
            return False, True
        else:
            return False, False
            
            
    #flashes the sequence for the player to copy
    def showSequence(self):
        for i in range(self.__currentDifficulty):
            if self.__answer[i]=="RED":
                print(self.__red)
            elif self.__answer[i]=="BLUE":
                print(self.__blue)
            elif self.__answer[i]=="GREEN":
                print(self.__green)
            elif self.__answer[i]=="YELLOW":
                print(self.__yellow)
            time.sleep(0)
            #makes sure all LEDs are off before showing the next LED
            self.__red.off()
            self.__green.off()
            self.__blue.off()
            self.__yellow.off()
    
    #checks the user input against the sequence returns False if it isn't the same
    def checkSequence(self):
        toBreak=False
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
                        return False, False
                    
                elif self.__blueButton.is_pressed:
                    pressed=True
                    if self.__answer[i]!="BLUE":
                        return False, False
                    
                elif self.___greenButton.is_pressed:
                    pressed=True
                    if self.__answer[i]!="GREEN":
                        return False, False
                    
                elif self.__yellowButton.is_pressed:
                    pressed=True
                    if self.__answer[i]!="YELLOW":
                        return False, False
                    
                elif self.__exitButton.is_pressed:
                    return False, True
                    
                    
        return True, False
                
        
        