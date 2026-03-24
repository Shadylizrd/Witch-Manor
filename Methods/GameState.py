import time
from MovementControls import *
from Puzzles import *
from Inventory import *

global BUTTONS
global INVENTORY
BUTTONS = MovementControls()
INVENTORY = Inventory


class GameState:
    def __init__(self, time_limit=300):
        # Main game state
        self.__state = "PLAYING"   # PLAYING / WON / LOST
        self.__puzzles = Puzzles()

        # Room state
        self.__rooms = self.__puzzles.getPuzzles()
        self.__currentRoom = 0
        self.__totalRooms = len(self.__rooms)

        # Timer
        self.__timeLimit = time_limit
        self.__startTime = time.time()

    # -------------------------
    # Timer methods
    # -------------------------
    def timeRemaining(self):
        elapsed = time.time() - self.__startTime
        remaining = int(self.__timeLimit - elapsed)
        if remaining < 0:
            remaining = 0
        return remaining

    def checkTimer(self):
        if self.timeRemaining() <= 0:
            self.__state = "LOST"

    # -------------------------
    # Room movement
    # -------------------------
    def move(self, direction):
        print(f"you walk away from room {self.__currentRoom}", end = " ")
        if direction == 0 or direction == 3:  # UP and RiGHT
            if self.__currentRoom < len(self.__rooms) - 1:
                self.__currentRoom += 1
                print(f"you walk towards door {self.__currentRoom}")
                print("")

        elif direction == 1 or direction == 2:  # DOWN and LEFT
            if self.__currentRoom > 0:
                self.__currentRoom -= 1
                print(f"you walk towards door {self.__currentRoom}")
                print("")


    # -------------------------
    # Room / puzzle info
    # -------------------------
    def getCurrentRoom(self):
        return self.__currentRoom

    def getCurrentPuzzle(self):
        return self.__rooms[self.__currentRoom][0]

    def roomSolved(self):
        return self.__puzzles.checkCompleted(self.__currentRoom)

    # -------------------------
    # Puzzle interaction
    # -------------------------
    def interact(self):
        currentPuzzle = self.getCurrentPuzzle()

        # Stop replaying solved rooms
        if self.roomSolved():
            currentPuzzle.solvedDescription()
            return

        passed = False
        # Will run the puzzle and intro text
        passed = currentPuzzle.enterRoom()

        # Update solved state and reward item
        if passed:
            self.__puzzles.setPassedPuzzles(self.__currentRoom)
            print(" ==> Puzzle solved!")
            print("")
            INVENTORY.addRelic()
        else:
            print(" ==> Puzzle failed or exited.")
            print("")

        self.checkWin()

    # -------------------------
    # Win / lose checks
    # -------------------------
    def checkWin(self):
        if INVENTORY.checkWin() == 5:
            return True
        return False
        

    def getState(self):
        return self.__state

    # -------------------------
    # Display methods
    # -------------------------
    def displayStatus(self):
        print("\n======================")
        print("ESCAPE ROOM")
        print("======================")
        print("Time remaining:", self.timeRemaining(), "seconds")
        print("Current room:", self.__currentRoom + 1, "/", self.__totalRooms)
        print("Solved:", self.roomSolved())
        print("Relics collected:", INVENTORY.checkWin)
        print("======================")

    # -------------------------
    # Main loop
    # -------------------------
    def run(self):
        print("Game started!")
        print(f"You stare down the hall... {self.__totalRooms} ahead of you")
        print("You must find all the relics before time runs out so that you may escape")
        print("")
        time.sleep(2)

        while self.__state == "PLAYING":
            self.checkTimer()

            if self.__state != "PLAYING":
                break

            self.displayStatus()

            userInput = BUTTONS.getInput()

            if userInput in [0, 1, 2, 3]:
                self.moveRoom(userInput)

            elif userInput == 4:
                self.interact()

        # End states
        if self.__state == "WON":
            print("\nYou escaped!")
            print("All 5 puzzles have been completed.")
            print("You collected all the relics and can make your great escape!")

        elif self.__state == "LOST":
            print("\nTime ran out! Game over.")


# -------------------------
# Run game
# -------------------------
if __name__ == "__main__":
    game = GameState(60)   # 60 seconds = 1 minutes // for testing purposes
    game.run()
