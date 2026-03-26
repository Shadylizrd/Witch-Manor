from GameState import *
import time
from Config import BUTTONS

class MainMenu:
    def __init__(self):

        self.options = ["Start Game", "Quit"] #tweak if more options needed
        self.currentOption = 0 #implement buttons to choose options
        self.game=GameState()

    #display menu in terminal
    def displayMenu(self):
        print("  Main Menu  ")
        for i in range(len(self.options)):
            if i == self.currentOption:
                print(" ==> " +self.options[i])
            else:
                print("   " + self.options[i])
    
    #Manouvreing through menu with button and loop
    def runMenu(self):
        while True:
            self.displayMenu()
            action = BUTTONS.getInput()

            if action== 0:
                if self.currentOption > 0:
                    self.currentOption -=1

            elif action == 1:
                if self.currentOption< len(self.options) -1:
                    self.currentOption +=1

            if action == 4:
                return self.options[self.currentOption]
            print("")
            time.sleep(0.1)
    #display results       
    def endScreen(self, won):
        print("   GAME OVER   ")
        if won:
            print("You escaped!")
        else:
            print("You failed to escape")

        print("Press INTERACT to return to the main menu.")

        while True:
            if BUTTONS.getInput() == 4:
                return

    #add game logic here or import from GameState
    def runGame(self):
        print(" Game commencing !!")
        time.sleep(2)
        self.game.run()
        return True

#create menu object
def main():
    menu = MainMenu()

    while True:
        choice = menu.runMenu()
    
        if choice == "Start Game":
            won = menu.runGame()
            menu.endScreen(won)

        elif choice =="Quit":
            print(" Quitting game.")
            break

#run only when file executed
if __name__ == "__main__":
    main()
