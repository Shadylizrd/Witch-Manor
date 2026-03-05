import time
import random
from gpiozero import LED, Button

blue = LED(17)
green = LED(27)
red = LED(22)
button = Button(23)

TIME_LIMIT = 2  # seconds
escaped = False

try:
    while not escaped:

        blue.off()
        green.off()
        red.off()

        print("Ready...")
        time.sleep(random.randint(1, 5))

        print("Now!")
        blue.on()

        start = time.time()

        button.wait_for_press()

        end = time.time()
        reaction = end - start

        blue.off()

        print("You reacted in", reaction, "seconds")

        if reaction <= TIME_LIMIT:
            print("Success! You escaped the room.")

            green.on()
            time.sleep(3)
            green.off()

            escaped = True   # stops the loop

        else:
            print("Too slow! Try again.")

            red.on()
            time.sleep(3)
            red.off()

except KeyboardInterrupt:
    print("Game stopped")
    blue.off()
    green.off()
    red.off()
