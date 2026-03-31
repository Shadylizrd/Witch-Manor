from gpiozero import Button, LED
import time

class MovementControls:
    def __init__(self):
        # Buttons connected to teh pins
        self.__upButton = Button(23)
        self.__downButton = Button(22)
        self.__leftButton = Button(27)
        self.__rightButton = Button(17)
        self.__interactButton = Button(4)

        #LED's 
        self.__led1 = LED(21)
        self.__led2 = LED(20)
        self.__led3 = LED(16)
        self.__led4 = LED(12)


    # continuously checks buttons and returns a string repressenting the action
    def moveRoom(self):
         while True:   # Checks if the switches are pressed and prevent button press being detected multiple times
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
        
            elif self.__interactButton.is_pressed:
                time.sleep(0.2)
                return 4
            
            
    def getInput(self):
         while True:   # Checks if the switches are pressed and prevent button press being detected multiple times
            if self.__upButton.is_pressed:
                return 0
        
            elif self.__downButton.is_pressed:
                return 1

            elif self.__leftButton.is_pressed:
                return 2

            elif self.__rightButton.is_pressed:
                return 3
        
            elif self.__interactButton.is_pressed:
                return 4
        
        #LED methods

    def led1(self):
        self.__led1.on()
        time.sleep(1)
        self.__led1.off()

    def led2(self):
        self.__led2.on()
        time.sleep(1)
        self.__led2.off()

    def led3(self):
        self.__led3.on()
        time.sleep(1)
        self.__led3.off()

    def led4(self):
        self.__led4.on()
        time.sleep(1)
        self.__led4.off()
