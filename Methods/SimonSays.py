import random
import gpiozero import LED, Button
import time
#takes a difficulty which is how many colours will be in the sequence

COLOURS=["RED", "BLUE", "GREEN", "YELLOW"]
class SimonSays(Puzzles):
    
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
        
        
        #setting up variables
        self.__answer=[]
        
        #put the difficulty in the Puzzles class
        self._difficulty=difficulty
        self.__currentDifficulty=0
        for i in range(difficulty):
            #makes a list of random colours the length of the difficulty
            self.__answer.append(COLOURS[random.randint(0,4)])
            
            
    #checks if the user has entered the entire sequence correctly
    #recoursively calls itself until the entire sequence is done
    def sequence(self):
        self.__currentDifficulty+=1
        #runs the number of times that the difficulty is 1 to difficulty
        showSequence()
        
        if checkSequence():
            if self._difficulty==self.__currentDifficulty:
                #returns true if the game has been won
                return True
            else:
                sequence()
        else:
            return False
            
            
    #flashes the sequence for the player to copy
    def showSequence(self):
        for i in range(self.__currentDifficulty):
            if answer[i]=="RED":
                self.__red.on()
            elif answer[i]=="BLUE":
                self.__blue.on()
            elif answer[i]=="GREEN":
                self.___green.on()
            elif answer[i]=="YELLOW":
                self.__yellow.on()
            time.sleep(2)
            #makes sure all LEDs are off before showing the next LED
            self.__red.off()
            self.__green.off()
            self.__blue.off()
            self.__yellow.off()
    
    #checks the user input against the sequence returns False if it isn't the same
    def checkSequence(self):
        
        #loops for each LED in sequence
        for i in range(self.__currentDifficulty):
            pressed=False
            #will loop until a button is pressed
            while pressed==False:
                
                #checks if each button is pressed then if that was the button that was supposed to be pressed
                if self.__redButton.is_pressed:
                    pressed=True
                    if answer[i]!="RED":
                        #returns False if it was not the correct button
                        return False
                    
                elif self.__blueButton.is_pressed:
                    pressed=True
                    if answer[i]!="BLUE":
                        return False
                    
                elif self.___greenButton.is_pressed:
                    pressed=True
                    if answer[i]!="GREEN":
                        return False
                    
                elif self.__yellowButton.is_pressed:
                    pressed=True
                    if answer[i]!="YELLOW":
                        return False
                    
        return True
                
        
        