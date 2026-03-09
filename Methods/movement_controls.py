from gpiozero import Button
from signal import pause

# Switches
up_pin = 23
down_pin = 22
left_pin = 27
right_pin = 17
interact_pin = 4

#buttons
up_button =Button(up_pin)
down_button = Button(down_pin)
left_button = Button(left_pin)
right_button =Button(right_pin)
interact_button=Button(interact_pin)

#Movement functions
def move_up():
    print("Move up")

def move_down():
    print("Move down")

def move_left():
    print("Move left")

def move_right():
    print("Move right")

def move_interact():
    print("Interact")

up_button.when_pressed =move_up
down_button.when_pressed = move_down
left_button.when_pressed = move_left
right_button.when_pressed = move_right
interact_button.when_pressed =move_interact

pause()