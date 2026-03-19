from ReadJson import *
from movement_controls import *

class KeyPuzzle():
    def __init__(self, trinketIndex, isPuzzleRoom):

        # buttons
        self.__buttons = MovementControls()
        self.__interact = self.__buttons.getInteract()
        
        #The type of puzzle so the Puzzles class can tell
        self.__type = "KEY"
        
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
        self.__isPuzzleRoom = isPuzzleRoom
        self.__solved = False 
        self.__taken = False
    
    def getType(self):
        return self.__type 
    
    def enterRoom(self, inventory):
        # checks which room type and runs the appropriate room?
        # could remove this method entirely and run it between puzzleRoom and keyRoom
        if self.__isPuzzleRoom:
            self.puzzleRoom(inventory)
        else:
            self.keyRoom(inventory)

    def puzzleRoom(self, inventory):
        if not self.__solved:
            print(self.__puzzleDescription)
            print("")
            if self.__interact.is_pressed:
                self.puzzleInteract(inventory)
        else:
            print(self.__solvedDescription)
            print("")

    def puzzleInteract(self, inventory):
        pressed = False
        if inventory.isEmpty():
            print(" ==> You don't have any items to use here")
        else:  
            while not pressed:  
                print(" ==> Select item:")
                print("")
                inventory.printInventory()
                # takes button input referring to place in inventory
                item = self.__buttons.getInput()
                trinket = inventory.remove(item)
                # checks that puzzle solve was successdful and adds a relic
                if self.giveTrinket(trinket):
                    inventory.addRelic()
                    # breaks out of the loop
                    pressed = True

                # other way to break out of loop
                if self.__interact.is_pressed:
                    pressed = True

    # call this method with the result of an inventory method as the 'trinket' parameter
    def giveTrinket(self, trinket):
        if trinket == self.__trinket:
            self.__solved = True
            print(self.__correctTrinket)
            return True
        else:
            print(self.__wrongTrinket)
            return False
                   

    def keyRoom(self, inventory):
        if not self.__taken:
            print(self.__trinketDescription)
            print(" ")
            if self.__interact.is_pressed:
                self.keyInteract(inventory)
        else:
            print(self.__takenDescription)
            print(" ")
        
    def keyInteract(self, inventory):
        inventory.add(self.__trinket)
        self.__taken = True
        
# inventory method or something
# when you interact list inventory items
# which item would you like to use?
# select via num input
# return 'trinket'