from Methods.MovementControls import MovementControls
import time

class MainMenu:
    def __init__(self):
        self.controls = MovementControls()
        self.options = ["Start Game", "Quit"] #tweak if more options needed
        self.currentOption = 0 #implement buttons to choose options
