from ReadJson import *
from gpiozero import LED, Button
import random

class KeyPuzzle():
    def __init__(self, trinketIndex):

        # buttons
        self.__left = Button(23)
        self.__up = Button(22)
        self.__down = Button(27)
        self.__right = Button(17)
        self.__interact = Button(4) 
  
        # will take a random digit from 0-4, generated along with the rest of the puzzles
        # these numbers need to be generated at the same time so puzzles don't repeat
        self.__trinketIndex = trinketIndex
        # uses the 'trinketIndex' here so that it doesn't need to be called in all the other attributes
        self.__keyDict = readJson('KeyDescriptions.json', 'trinkets')[trinketIndex]

        # initialising all the main attributes of the class
        self.__trinket = self.__keyDict['trinket']
        self.__trinketDescription = self.__keyDict['trinketDescription']
        self.__puzzleDescription = self.__keyDict['puzzleDescription']
        self.__solvedDescription = self.__keyDict['solvedDescription']
        self.__correctTrinket = self.__keyDict['correctTrinket']
        self.__wrongTrinket = self.__keyDict['wrongTrinket']

        self.__solved = False 

    # returns the main trinket
    def getTrinket(self):
        return self.__trinket
    
    # call this method with the result of an inventory method as the 'trinket' parameter
    def giveTrinket(self, trinket):
        if trinket == self.__trinket:
            self.__solved = True
            return self.__correctTrinket
        else:
            return self.__wrongTrinket
    
    def enterRoom(self):
        if self.__solved == False:
            print(self.__puzzleDescription)
            if self.__interact.is_pressed:
                # should be something like trinket = openInventory() --> returns a trinket
                trinket = input("Which item would you like to use?")
                self.giveTrinket(trinket)
        else:
            print(self.__solvedDescription)

        

puzzleKey1 = KeyPuzzle(0)
print(puzzleKey1.getTrinket())

# inventory method or something
# when you interact list inventory items
# which item would you like to use?
# select via num input
# return 'trinket'