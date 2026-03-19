class Inventory():
    def __init__(self):
        self.__inventory = []
        # winning condition (collect 5 to win)
        self.__numRelics = 0


    def add(self, object):
        self.__inventory.append(object)

    def remove(self, item):
        return self.__inventory.pop(item)

    def getRelics(self):
        return self.__numRelics
    
    def printInventory(self):
        for i in self.__inventory:
            print(f"==> {i}")

inventory = Inventory()

inventory.add("cat")
inventory.add("dog")
inventory.add("meow")

inventory.printInventory()

print(inventory.remove(1))