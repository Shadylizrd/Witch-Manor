from ReadJson import *
import random

class KeyPuzzle():
    def __init__(self, trinketIndex):
  
        # will take a random digit from 0-4, generated along with the rest of the puzzles
        # these numbers need to be generated at the same time so puzzles don't repeat
        self.__trinketIndex = trinketIndex
        self.__keyDict = readJson('KeyDescriptions.json', 'trinkets')[trinketIndex]

        self.__trinket = self.__keyDict['trinket']
        self.__trinketDescription = self.__keyDict['trinketDescription']
        self.__puzzleDescription = self.__keyDict['puzzleDescription']
        self.__solvedDescription = self.__keyDict['solvedDescription']
        self.__correctTrinket = self.__keyDict['correctTrinket']
        self.__wrongTrinket = self.__keyDict['wrongTrinket']

    def getTrinket(self):
        return self.__trinket
        

puzzleKey1 = KeyPuzzle(0)
print(puzzleKey1.getTrinket())