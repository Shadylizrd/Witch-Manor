import time
import random
from gpiozero import LED, Button


class ReactionGame:
    def __init__(self, timeLimit=2):
        # LEDs
        self.__blue = LED(21)
        self.__green = LED(20)
        self.__red = LED(16)

        # Button
        self.__button = Button(17)

        # Game settings
        self.__timeLimit = timeLimit
        self.__type = "REACTION"

    # so Puzzles.py can identify it
    def getType(self):
        return self.__type

    # main game logic
    def sequence(self):
        try:
            while True:
                # reset LEDs
                self.__blue.off()
                self.__green.off()
                self.__red.off()

                print("Ready...")
                time.sleep(random.randint(1, 5))

                print("Now!")
                self.__blue.on()

                start = time.time()

                self.__button.wait_for_press()

                end = time.time()
                reaction = end - start

                self.__blue.off()

                print("You reacted in", reaction, "seconds")

                if reaction <= self.__timeLimit:
                    print("Success! You escaped the room.")

                    self.__green.on()
                    time.sleep(2)
                    self.__green.off()

                    return True   # puzzle solved

                else:
                    print("Too slow! Try again.")

                    self.__red.on()
                    time.sleep(2)
                    self.__red.off()

        except KeyboardInterrupt:
            print("Game stopped")
            self.__blue.off()
            self.__green.off()
            self.__red.off()
            return False
