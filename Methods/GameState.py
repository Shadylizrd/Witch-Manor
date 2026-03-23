import time
from MovementControls import *
from Puzzles import *

global BUTTONS
BUTTONS = MovementControls()

class GameState:
    def __init__(self, time_limit=300):
        # Main game state
        self.__state = "PLAYING"   # PLAYING / WON / LOST
        self.__controls = MovementControls()
        self.__puzzles = Puzzles()

        # Room state
        self.__rooms = self.__puzzles.getPuzzles()
        self.__currentRoom = 0
        self.__totalRooms = len(self.__rooms)

        # Rewards / flavour items
        self.__itemsCollected = []

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
        if direction == 0:  # UP
            if self.__currentRoom < len(self.__rooms) - 1:
                self.__currentRoom += 1

        elif direction == 1:  # DOWN
            if self.__currentRoom > 0:
                self.__currentRoom -= 1

        elif direction == 2:  # LEFT
            if self.__currentRoom > 0:
                self.__currentRoom -= 1

        elif direction == 3:  # RIGHT
            if self.__currentRoom < len(self.__rooms) - 1:
                self.__currentRoom += 1

    # -------------------------
    # Room / puzzle info
    # -------------------------
    def getCurrentRoom(self):
        return self.__currentRoom

    def getCurrentPuzzle(self):
        return self.__rooms[self.__currentRoom]

    def roomSolved(self):
        return self.__puzzles.checkCompleted(self.__currentRoom)

    # -------------------------
    # Puzzle interaction
    # -------------------------
    def interact(self):
        currentPuzzle = self.getCurrentPuzzle()

        # Stop replaying solved rooms
        if self.roomSolved():
            print("This room has already been solved")
            return

        passed = False

        # Simon Says object
        if hasattr(currentPuzzle, "getType"):
            if currentPuzzle.getType() == "SIMON":
                print("Starting Simon Says puzzle...")
                passed = currentPuzzle.sequence()

            elif currentPuzzle.getType() == "KEY":
                print("Starting Key puzzle...")
                # placeholder if a real KEY class is added later
                passed = True

        # If the puzzle was stored as the string "KEY"
        elif currentPuzzle == "KEY":
            print("Starting Key puzzle...")
            # placeholder until KeyPuzzle is fully connected
            passed = True

        # Update solved state and reward item
        if passed:
            self.__puzzles.setPassedPuzzles(self.__currentRoom)
            itemName = "Item from Room " + str(self.__currentRoom + 1)
            self.__itemsCollected.append(itemName)
            print("Puzzle solved!")
            print("You collected:", itemName)
        else:
            print("Puzzle failed or exited.")

        self.checkWin()

    # -------------------------
    # Win / lose checks
    # -------------------------
    def checkWin(self):
        if self.__puzzles.completedPuzzles():
            self.__state = "WON"

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
        print("Items collected:", len(self.__itemsCollected))
        print("======================")

    # -------------------------
    # Main loop
    # -------------------------
    def run(self):
        print("Game started!")

        while self.__state == "PLAYING":
            self.checkTimer()

            if self.__state != "PLAYING":
                break

            self.displayStatus()

            userInput = BUTTONS.getInput()

            if userInput in ["UP", "DOWN", "LEFT", "RIGHT"]:
                self.moveRoom(userInput)

            elif userInput == "INTERACT":
                self.interact()

        # End states
        if self.__state == "WON":
            print("\nYou escaped!")
            print("All 5 puzzles have been completed.")
            print("Items collected:", self.__itemsCollected)

        elif self.__state == "LOST":
            print("\nTime ran out! Game over.")


# -------------------------
# Run game
# -------------------------
if __name__ == "__main__":
    game = GameState(60)   # 60 seconds = 1 minutes // for testing purposes
    game.run()
