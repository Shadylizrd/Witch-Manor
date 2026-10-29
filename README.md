# Witch Manor🔮🐈‍⬛
An escape room game built on a Raspberry Pi, utilizing buttons and LEDs

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

### Team
This was a group project. Contributors:
- Rhiannon Summers
- Ray Baker
- Myan Patel
- Samyok Limbu