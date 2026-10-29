# Witch Manor🔮🐈‍⬛
An escape room game built on a Raspberry Pi, utilizing buttons and LEDs

This project is an escape room game that runs on a Raspberry Pi 5 and is controlled by five
GPIO buttons. We also used four LEDs to display puzzle outputs and one LED to represent
the in-game timer. The rest of the game's outputs are printed to the terminal, but all
interaction is handled via the GPIO buttons.

The player's objective is to solve all generated puzzles within the time limit and collect five
relics to win. The game offers two puzzle types: Simon Says and "lock and key." In Simon
Says, the LEDs light up in a sequence, adding one more step to the sequence each time
the pattern is repeated back correctly until the maximum complexity is reached. For the
"lock and key" puzzles, the player must collect a trinket from one room and bring it to the
puzzle's matching room

### Features
- Randomised manor: the room order and the puzzles are shuffled every playthrough - like a roguelike!
- Simon Says puzzles: watch a sequence flash on the red/blue/green/yellow LEDs, then repeat it on the buttons. Each sequence longer than the last.
- Key puzzles: find a trinket in one room and use it to solve a problem in another, using a simple inventory system.
- Live countdown: a 5-minute timer, with a little LED that flashes faster as the time runs out.
- Story description data: room and item descriptions are stored in JSON, so new rooms can be written without touching the code

### How to play!
- Use Up/Down to pick Start Game on the main menu and press Interact.
- Move between rooms with the direction buttons (Up/Right go forward, Down/Left go back).
- Press Interact to investigate a room.
- Simon Says rooms: watch the LEDs, then press the matching buttons in order. If you get it wrong a new sequence is generated. You can also press interact to exit the game.
- Key rooms: pick up the trinket you find, then bring it to a room where you think it could be useful, you need only select it from your inventory once in the room.
- Every solved puzzle earns a relic. Collect 5 relics before the timer hits zero to escape!

### Project structure
```
src/
├── MainMenu.py          # Entry point: main menu, start/quit, end screen
├── GameState.py         # Game loop, room movement, timer + timer LED, win/lose
├── Puzzles.py           # Generates and shuffles the set of puzzles for a run
├── SimonSays.py         # LED sequence memory puzzle
├── KeyPuzzle.py         # Find-the-item / use-the-item puzzle (puzzle room + key room)
├── Inventory.py         # Player inventory and relic count
├── MovementControls.py  # GPIO buttons and LEDs (gpiozero)
├── Config.py            # Shared INVENTORY and BUTTONS instances
├── ReadJson.py          # Loads room text from JSON
└── GameData/
    ├── SimonDescriptions.json  # Text for Simon Says rooms
    └── KeyDescriptions.json    # Trinkets and text for key rooms
```
### Raspberry Pi Hardware!
<img width="4000" height="3000" alt="20260305_115140" src="https://github.com/user-attachments/assets/737ce590-8bf3-472c-92b0-f23a1509e324" style="width:50%; height:auto; object-position:right;"/>
<img width="4000" height="3000" alt="20260305_115151" src="https://github.com/user-attachments/assets/3d1711c9-92da-4265-8372-9f7f68fa9280" 
style="width:50%; height:auto; object-position:right;"/>

### Team
This was a group project. Contributors:
- Rhiannon Summers
- Ray Baker
- Myan Patel
- Samyok Limbu
