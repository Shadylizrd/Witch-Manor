import random
from gpiozero import LED, Button
import time

class codePuzzle():
    def __init__(self):
        self.__code=[]
        for i in range (4):
            self.__code.append(random.randint(0,9))
    def getCode(self):
        return self.__code