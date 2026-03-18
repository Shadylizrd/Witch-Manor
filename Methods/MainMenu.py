from Methods.MovementControls import MovementControls
import time

class MainMenu:
    def __init__(self):#This defines a method called get_input.Its job is to check the buttons and return the player's action. The method belongs to the class, so it needs self.
        self.controls = MovementControls()
        self.options = ["Start Game", "Quit"] #tweak if more options needed
        self.currentOption = 0 #implement buttons to choose options

    #display menu in terminal
    def displayMenu(self):
        print("  Main Menu  ")
        for i in range(len(self.options)):
            if i == self.currentOption:
                print(" ==> " +self.options[i])
            else:
                print("   " + self.options[i])

    def runMenu(self):
        while True:
            self.displayMenu()
            action = self.controls.getInput()

            if action== "UP":
                if self.currentOption > 0:
                    self.currentOption -=1

            elif action == "DOWN":
                if self.currentOption< len(self.options) -1:
                    self.currrentOption +=1

            elif action == "INTERACT":
                return self.options[self.currentOption]
            
            time.sleep(0.1)
                

