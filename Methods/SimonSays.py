import random
import gpiozero import LED, Button
import time

COLOURS=["RED", "BLUE", "GREEN", "YELLOW"]
class SimonSays(Puzzles):
    
    def __init__(self,difficulty):
        #setting up the I/O
        self.__red=LED(22)
        self.__green=LED(27)
        self.__blue=LED(17)
        self.__yellow=LED(32)
        
        #setting up variables
        self.__answer=[]
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
        
        if self._difficulty==self.__currentDifficulty:
            #returns true if the game has been won
            return True
        else:
            sequence()
            
            
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
    
        
        
        