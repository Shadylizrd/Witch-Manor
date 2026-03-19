from gpiozero import Button
import time

class MovementControls:
    def __init__(self):
        # Buttons connected to teh pins
        self.__upButton = Button(23)
        self.__downButton = Button(22)
        self.__leftButton = Button(27)
        self.__rightButton = Button(17)
        self.__interactButton = Button(4)

    # continuously checks buttons and returns a string repressenting the action
    def getInput(self):
            # Checks if the switches are pressed and prevent button press being detected multiple times
        if self.__upButton.is_pressed:
            time.sleep(0.2) 
            return 0
        elif self.__downButton.is_pressed:
            time.sleep(0.2)
            return 1

        elif self.__leftButton.is_pressed:
            time.sleep(0.2)
            return 2

        elif self.__rightButton.is_pressed:
            time.sleep(0.2)
            return 3

        return None
            
    def getInteract(self):
        if self.__interactButton.is_pressed:
            time.sleep(0.2)
            return 4
        return None