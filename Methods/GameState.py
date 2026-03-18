import time
from Methods.MovementControls import MovementControls
from Puzzles import Puzzles


class GameState:
    def __init__(self, timeLimit=300):
        self.__state = "PLAYING"

        self.__controls = MovementControls()
        self.__puzzles = Puzzles()

        self.__rooms = self.__puzzles.getPuzzles()
        self.__currentRoom = 0

        self.__timeLimit = timeLimit
        self.__startTime = time.time()

    # -------------------------
    # Timer
    # -------------------------
    def timeRemaining(self):
        return int(self.__timeLimit - (time.time() - self.__startTime))

    def checkTimer(self):
        if self.timeRemaining() <= 0:
            self.__state = "LOST"

    # -------------------------
    # Movement
    # -------------------------
    def move(self, direction):
        if direction in ["RIGHT", "UP"]:
            if self.__currentRoom < len(self.__rooms) - 1:
                self.__currentRoom += 1

        elif direction in ["LEFT", "DOWN"]:
            if self.__currentRoom > 0:
                self.__currentRoom -= 1

    # -------------------------
    # Interaction
    # -------------------------
    def interact(self):
        currentPuzzle = self.__rooms[self.__currentRoom][0]

        # find index in puzzle system
        index = self.__currentRoom

        # skip if already solved
        if self.__puzzles.checkCompleted(index):
            print("Already completed this room.")
            return

        print("Interacting with room", index + 1)

        passed = False

        if currentPuzzle.getType() == "SIMON":
            passed = currentPuzzle.sequence()

        elif currentPuzzle.getType() == "KEY":
            currentPuzzle.enterRoom()
            # KEY puzzle manages its own state, assume solved handled internally
            passed = True  # you can refine this later

        if passed:
            self.__puzzles.setPassedPuzzles(index)
            print("Room solved!")

        self.checkWin()

    # -------------------------
    # Win check
    # -------------------------
    def checkWin(self):
        if self.__puzzles.completedPuzzles():
            self.__state = "WON"

    # -------------------------
    # Display
    # -------------------------
    def display(self):
        print("\n====================")
        print("Room:", self.__currentRoom + 1)
        print("Time:", self.timeRemaining())
        print("Solved:", self.__puzzles.checkCompleted(self.__currentRoom))
        print("====================")

    # -------------------------
    # Main loop
    # -------------------------
    def run(self):
        print("Game started!")

        while self.__state == "PLAYING":
            self.checkTimer()

            if self.__state != "PLAYING":
                break

            self.display()

            action = self.__controls.getInput()

            if action in ["UP", "DOWN", "LEFT", "RIGHT"]:
                self.move(action)

            elif action == "INTERACT":
                self.interact()

        if self.__state == "WON":
            print("\nYOU ESCAPED!")

        elif self.__state == "LOST":
            print("\nTIME RAN OUT!")


# run
if __name__ == "__main__":
    game = GameState()
    game.run()