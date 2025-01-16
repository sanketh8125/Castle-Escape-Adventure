# Castle Escape Adventure

## Installation
1. Clone the repository or download the code.
2. Ensure you have Python 3.x installed on your system.
3. Run the script using the command:
   ```bash
   python Castle_Escape_Adventure.py
   ```

## Description
Castle Escape Adventure is an interactive text-based adventure game where the player creates a character and navigates through a mysterious castle filled with puzzles. The goal is to escape the castle by solving puzzles and making the right choices. The game includes multiple rooms, each with a unique challenge that the player must overcome to progress.

## Features
- **Character Creation**: Players can create their character by choosing a name and role.
- **Puzzle Rooms**: Each room has a different puzzle or challenge to solve.

## How to Play
1. **Character Creation**: The player will input a name and select a role (warrior, mage, or rogue). If an invalid role is selected, the default role is "warrior."
2. **Game Progression**: The player navigates through different rooms, each with its own puzzle.
   - **Room 1**: A hallway with three doors, only one of which leads to safety.
   - **Room 2**: A puzzle room where players must solve a math puzzle to unlock a box.
   - **Library Room**: A room where the player must solve a puzzle written in a glowing book to proceed.
   - **Final Room**: A large door with a riddle that must be solved to escape the castle.

## Code Overview

### Functions

#### `character_creation()`
- Prompts the player to enter their character's name and choose a role.
- Valid roles are "warrior", "mage", and "rogue". Invalid roles default to "warrior".
- Returns the character's name and role as a tuple.

#### `intro()`
- Displays the game's introduction and sets the scene.
- Provides instructions for beginning the adventure.

#### `room_one()`
- The first room of the game, a hallway with three doors.
- The player chooses one of the shuffled doors to proceed.
- A correct choice leads to the next room, while a wrong choice ends the game.

#### `room_two()`
- The second room, a puzzle room.
- The player must solve a math puzzle to unlock a box and proceed.

#### `library_room()`
- A library room with a glowing book that contains a math puzzle.
- The player must solve the puzzle to obtain a key and continue.

#### `room_three_with_twist()`
- The final room, where the player must solve a riddle to unlock the door and escape the castle.
- A correct answer results in victory, while an incorrect answer ends the game.

#### `main()`
- The main function that runs the game.
- Handles character creation, introduction, and room transitions.
- Displays the appropriate end message based on the player's success or failure.
