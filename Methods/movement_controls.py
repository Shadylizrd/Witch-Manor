
from gpiozero import Button
import time

#tring to fix an issue
class MovementControls:
    def __init__(self):
        # Buttons connected to teh pins
        self.__up_button = Button(23)
        self.__down_button = Button(22)
        self.__left_button = Button(27)
        self.__right_button = Button(17)
        self.__interact_button = Button(4)

    # continuously checks buttons and returns a string repressenting the action
    def get_input(self):
        while True:

            # Checks if the switches are pressed and prevent button press being detected multiple times
            if self.__up_button.is_pressed:
                time.sleep(0.2) 
                return "UP"

            elif self.__down_button.is_pressed:
                time.sleep(0.2)
                return "DOWN"

            elif self.__left_button.is_pressed:
                time.sleep(0.2)
                return "LEFT"

            elif self.__right_button.is_pressed:
                time.sleep(0.2)
                return "RIGHT"

            elif self.__interact_button.is_pressed:
                time.sleep(0.2)
                return "INTERACT"