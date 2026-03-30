from ReadJson import *
from Config import INVENTORY
from Config import BUTTONS

class KeyPuzzle():
    def __init__(self, puzzleIndex, isPuzzleRoom):
        
        #The type of puzzle so the Puzzles class can tell
        self.__type = "KEY"
        
        # will take a random digit from 0-4, generated along with the rest of the puzzles
        # uses the 'trinketIndex' here so that it doesn't need to be called in all the other attributes
        self.__keyDict = readJson('KeyDescriptions.json', 'trinkets')[puzzleIndex]

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
    
    def getType(self):
        return self.__type 

    def puzzleRoom(self):
        return self.__isPuzzleRoom
            
    def solvedDescription(self):
        print(self.__solvedDescription)
    
    def enterRoom(self, gameState):
        # checks which room type and runs the appropriate room?
        # could remove this method entirely and run it between puzzleRoom and keyRoom
        if self.__isPuzzleRoom == "puzzleRoom":
            self.puzzleRoom(gameState)
        if self.__isPuzzleRoom == "keyRoom":
            self.keyRoom(gameState)
        return self.__solved

    def puzzleRoom(self, gameState):
        print(self.__puzzleDescription)
        print("")
        if BUTTONS.getInput() == 4:
            self.puzzleInteract(gameState)

    def puzzleInteract(self, gameState):
        pressed = False
        if INVENTORY.isEmpty():
            print(" ==> You don't have any items to use here")
        else:  
            print(" ==> Select item:\n")
            INVENTORY.printInventory()
            
            while not pressed:  
                # Keeps timer + LED updating during puzzle
                gameState.tick()
                item = BUTTONS.getInput()

                # breaks out of the loop
                if BUTTONS.getInput() == 4:
                    pressed = True
                    break

                trinket = INVENTORY.remove(item)
                # checks that puzzle solve was successdful and adds a relic
                if trinket is not None:
                    if self.giveTrinket(trinket):
                        # breaks out of the loop
                        pressed = True

               

    # call this method with the result of an  method as the 'trinket' parameter
    def giveTrinket(self, trinket):
        if trinket == self.__trinket:
            self.__solved = True
            print(self.__correctTrinket)
            return True
        else:
            print(self.__wrongTrinket)
            return False
                   

    def keyRoom(self, gameState):
        if not self.__solved:
            print(self.__trinketDescription)
            print(" ")
            if BUTTONS.getInput() == 4:
                self.keyInteract()
        else:
            print(self.__takenDescription)
            print(" ")
        
    def keyInteract(self):
        INVENTORY.add(self.__trinket)
        self.__solved = True