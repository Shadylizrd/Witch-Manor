from KeyPuzzle import *
0
class Inventory():
    def __init__(self):
        self.__inventory = []
        # winning condition (collect 5 to win)
        self.__numRelics = 0

    def addRelic(self):
        self.__numRelics += 1
        print(f" ==> you now have {self.__numRelics} relics!")

    # once this equals 5 then you should win the game
    # run this method each time you pick up a relic
    def checkRelics(self):
        return self.__numRelics
    
    # simple add and remove methods
    def add(self, object):
        print(f" ==> added {object} to your inventory!")
        self.__inventory.append(object)

    def remove(self, item):
        # exits out of the method
        if self.isEmpty():
            return
        try:
            popped = self.__inventory.pop(item)
        except IndexError:
            print(" ==> you don't have an item stored there...")
            return
        return popped

    
    def printInventory(self):
        print(" -- Your Inventory -- ")
        for i in self.__inventory:
            print(f" ==> {i}")

    def isEmpty(self):
        return len(self.__inventory) == 0
inventory = Inventory()

room1 = KeyPuzzle(0, True)
room2 = KeyPuzzle(0, False)

room1.enterRoom(inventory)
room2.enterRoom(inventory)

room1.enterRoom(inventory)
room2.enterRoom(inventory)