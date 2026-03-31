from gpiozero import LED
import time
import random
from Puzzles import *
from Config import INVENTORY
from Config import BUTTONS

class GameState:
    def __init__(self, time_limit=300):
        # Main game state
        self.__state = "PLAYING"
        self.__puzzles = Puzzles()

        # Room state
        # randomises the layout of the rooms
        self.__rooms = []
        tempPuzzles = self.__puzzles.getPuzzles().copy()
        for i in range(len(tempPuzzles)):
            num = random.randint(0, len(tempPuzzles) - 1)
            self.__rooms.append(tempPuzzles[num])
            tempPuzzles.pop(num)

        self.__currentRoom = 0
        self.__totalRooms = len(self.__rooms)

        # Timer
        self.__timeLimit = time_limit
        self.__startTime = None

        # LED Flash Timer
        self.__timerLed = LED(14)
        self.__lastFlashTime = time.time()
        self.__ledState = False

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
    
    def tick(self):
        self.checkTimer()
        self.updateTimerLed()

    def timerLedOn(self):
        self.__timerLed.on()

    def timerLedOff(self):
        self.__timerLed.off()

    def updateTimerLed(self):
        remaining = self.timeRemaining()

        if remaining > 40:
            flashRate = 1.0
        elif remaining > 20:
            flashRate = 0.5
        elif remaining > 10:
            flashRate = 0.25
        else:
            flashRate = 0.1

        currentTime = time.time()

        if currentTime - self.__lastFlashTime >= flashRate:
            self.__lastFlashTime = currentTime

            if self.__ledState:
                self.timerLedOff()
                self.__ledState = False
            else:
                self.timerLedOn()
                self.__ledState = True

    # -------------------------
    # Room movement
    # -------------------------
    def move(self, direction):
        print("")
        print(f"you walk away from room {self.__currentRoom + 1}", end=" ")

        if direction == 0 or direction == 3:  # UP and RIGHT
            if self.__currentRoom < self.__totalRooms - 1:
                self.__currentRoom += 1
                print(f"you walk towards room {self.__currentRoom + 1}")
                print("")

        elif direction == 1 or direction == 2:  # DOWN and LEFT
            if self.__currentRoom > 0:
                self.__currentRoom -= 1
                print(f"you walk towards room {self.__currentRoom + 1}")
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

        passed = currentPuzzle.enterRoom(self)

        # Update solved state and reward item
        if passed:
            self.__puzzles.setPassedPuzzles(self.__currentRoom)
            print(" ==> Room solved!")
            print("")
            if currentPuzzle.getRoomType() == "puzzleRoom":
                INVENTORY.addRelic()
        else:
            print(" ==> Puzzle failed or exited.")
            print("")

        if self.checkWin():
            self.__state = "WON"

    # -------------------------
    # Win / lose checks
    # -------------------------
    def checkWin(self):
        return INVENTORY.checkWin() == 5

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
        print("Relics collected:", INVENTORY.checkWin())
        print("======================")

    # -------------------------
    # Main loop
    # -------------------------
    def run(self):
        print("Game started!")
        print(f"You stare down the hall... {self.__totalRooms} rooms ahead of you")
        print("You must find all the relics before time runs out so that you may escape")
        print("")
        self.__startTime = time.time()
        self.displayStatus()
        time.sleep(2)
        print("")
        print("Press up/down to navigate and x to interact")

        print("You face room 1...")

        while self.__state == "PLAYING":
            self.checkTimer()

            if self.__state != "PLAYING":
                break

            self.updateTimerLed()

            userInput = BUTTONS.moveRoom()

            if userInput in [0, 1, 2, 3]:
                self.move(userInput)
                self.displayStatus()

            elif userInput == 4:
                self.interact()
                self.displayStatus()

            time.sleep(0.05)

        self.timerLedOff()

        if self.__state == "WON":
            print("\nYou escaped!")
            print("All 5 puzzles have been completed.")
            print("You collected all the relics and can make your great escape!")

        elif self.__state == "LOST":
            print("\nTime ran out! Game over.")


if __name__ == "__main__":
    game = GameState(60)
    game.run()
                                  