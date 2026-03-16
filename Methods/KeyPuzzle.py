from ReadJson import *
from gpiozero import LED, Button
import random

class KeyPuzzle():
    def __init__(self, trinketIndex, puzzleRoom):

        # buttons
        self.__interact = Button(4)  
  
        # will take a random digit from 0-4, generated along with the rest of the puzzles
        # these numbers need to be generated at the same time so puzzles don't repeat
        self.__trinketIndex = trinketIndex
        # uses the 'trinketIndex' here so that it doesn't need to be called in all the other attributes
        self.__keyDict = readJson('KeyDescriptions.json', 'trinkets')[trinketIndex]

        # initialising all the main attributes of the class
        self.__trinket = self.__keyDict['trinket']
        self.__trinketDescription = self.__keyDict['trinketDescription']
        self.__takenDescription = self.__keyDict['takenDescription']
        self.__puzzleDescription = self.__keyDict['puzzleDescription']
        self.__solvedDescription = self.__keyDict['solvedDescription']
        self.__correctTrinket = self.__keyDict['correctTrinket']
        self.__wrongTrinket = self.__keyDict['wrongTrinket']

        # extra attributes for state of room
        # puzzleRoom checks whether the room conatins the puzzle or the key
        self.__puzzleRoom = puzzleRoom
        self.__solved = False 
        self.__taken = False
    
    # call this method with the result of an inventory method as the 'trinket' parameter
    def giveTrinket(self, trinket):
        if trinket == self.__trinket:
            self.__solved = True
            print(self.__correctTrinket)
        else:
            print(self.__wrongTrinket)
    
    def enterRoom(self):
        if self.__puzzleRoom:
            if not self.__solved:
                print(self.__puzzleDescription)
                if self.__interact.is_pressed:
                    # should be something like trinket = openInventory() --> returns a trinket
                    trinket = input("Which item would you like to use?\n")
                    # placeholder ^^^
                    self.giveTrinket(trinket)
            else:
                print(self.__solvedDescription)
        else:
            if not self.__taken:
                print(self.__trinketDescription)
                if self.__interact.is_pressed:
                    # add trinket into inventory
                    # addInventory() or something
                    self.__taken = True
            else:
                print(self.__takenDescription)

        
# inventory method or something
# when you interact list inventory items
# which item would you like to use?
# select via num input
# return 'trinket'