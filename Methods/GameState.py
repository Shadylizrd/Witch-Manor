import time

# Initialising all the rooms
roomsList = [reactionRoom, simonSays, rpg, room4, room5]
currentRoom = 0

# Timer setup
startTime = time.time()
timeLimit = 60  # seconds

def gameTimer():
    # Returns True if time is remaining, False if time ran out
    return (time.time() - startTime) <= timeLimit


def move(currentRoom, direction, roomsList):
    if direction == "up":
        currentRoom += 1
    elif direction == "down":
        currentRoom -= 1

    # Prevent going out of array bounds
    currentRoom = max(0, min(currentRoom, len(roomsList) - 1))
    return currentRoom


def interact(currentRoom, roomsList):
    # Call the play() function from the current room
    solved = roomsList[currentRoom].play()

    if solved:
        print("Puzzle solved")
    else:
        print("Try again")


# Main game loop with timer
while gameTimer():
    remaining = int(timeLimit - (time.time() - startTime))
    print(f"\nTime remaining: {remaining} seconds")
    print(f"You are in Room {currentRoom + 1}")

    action = input("Do you want to move or interact? ").lower()

    if action == "move":
        direction = input("Move up or down: ").lower()
        currentRoom = move(currentRoom, direction, roomsList)

    elif action == "interact":
        interact(currentRoom, roomsList)

    else:
        print("Invalid action. Type 'move' or 'interact'.")

print("\nTime ran out! Game over.")
