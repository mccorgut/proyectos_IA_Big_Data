# Rock-Paper-Scissors-Lizard-Spock Game

This program is a Python-based game where the user competes against the computer in a variation of the classic "Rock-Paper-Scissors" game, adding two additional options: Lizard and Spock. The game follows specific rules of winning, losing, and tying, which are defined in an XML file (`victories.xml`).

## Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [XML Victory Conditions](#xml-victory-conditions)
4. [Code Structure](#code-structure)
5. [Detailed Code Explanation](#detailed-code-explanation)
    - [Import Statements](#import-statements)
    - [Enums for Game Actions and Results](#enums-for-game-actions-and-results)
    - [Global Variables](#global-variables)
    - [Function Explanations](#function-explanations)
6. [Running the Game](#running-the-game)

---

## Overview

The program is a console-based game where:
- The user chooses one of five actions: Rock, Paper, Scissors, Lizard, or Spock.
- The computer responds with its own choice, based on a prediction algorithm that considers the user's recent actions.
- Game outcomes are determined using rules defined in an XML file, which outlines which actions beat others.
- The program displays the result of each round and allows the user to continue or stop.

## Requirements

- Python 3.x
- `victories.xml`: An XML file defining the conditions for victory, which is required to determine which action beats another.

## XML Victory Conditions

The XML file `victories.xml` contains the rules for victory conditions in the game. Each victory condition specifies an action and the action it defeats. An example structure could be:

```xml
<victories>
    <victory choice="Rock" against="Scissors"/>
    <victory choice="Rock" against="Lizard"/>
    <victory choice="Paper" against="Rock"/>
    <victory choice="Paper" against="Spock"/>
    <!-- Additional conditions for all possible outcomes -->
</victories>
```

The program loads this file at the start and uses it to check who wins each round based on the chosen actions.

## Code Structure

The code is organized as follows:
1. **Imports**: Imports required libraries, including `random`, `IntEnum`, and `ElementTree` for XML parsing.
2. **GameAction and GameResult Enums**: Define possible actions and outcomes.
3. **Functions**:
   - `assess_game()`: Evaluates the game result based on user and computer actions.
   - `get_computer_action()`: Chooses the computer’s action, factoring in the user’s recent choices.
   - `get_user_action()`: Collects the user’s choice.
   - `get_random_computer_action()`: Selects a random action for the computer if there’s no pattern in the user's choices.
   - `get_winner_action()`: Determines the winning action against a given action.
   - `play_another_round()`: Asks if the user wants to continue playing.
   - `main()`: Main function, which runs the game loop and tracks user history.

## Detailed Code Explanation

### Import Statements

```python
import random
from enum import IntEnum
from statistics import mode
from xml.etree import ElementTree
```

- `random`: Used to generate random choices for the computer.
- `IntEnum`: Used to define enums with integer values for game actions and results.
- `mode`: Calculates the most frequent item in a list, helping predict the user's next choice.
- `ElementTree`: Parses the XML file containing victory conditions.

### Enums for Game Actions and Results

#### GameAction Enum

```python
class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4
```

Defines possible actions in the game, making each action a unique integer for easier comparison.

#### GameResult Enum

```python
class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2
```

Defines possible results (Victory, Defeat, Tie) to represent the outcome of each round.

### Global Variables

```python
NUMBER_RECENT_ACTIONS = 5
```

This constant determines how many of the user’s recent actions are considered when predicting their next choice.

```python
Victories = ElementTree.parse('victories.xml').getroot()
```

Loads the XML file with victory conditions, storing it as a root element for future lookups.

### Function Explanations

#### `assess_game(user_action, computer_action)`

```python
def assess_game(user_action, computer_action):
```

- **Purpose**: Checks the game result by comparing the user’s action with the computer’s action.
- **Logic**:
  - If the actions are the same, it’s a tie.
  - If the user’s action beats the computer’s action (determined by querying the XML), the user wins.
  - Otherwise, the computer wins.

### Key Changes Explained

1.  **Extracting the Victory Message**:
    
    -   After checking for a victory in the XML (`victory_element = Victories.find(victory_path)`), we retrieve the text of that victory condition with `victory_message = victory_element.text.strip()`. This extracts the descriptive text you provided in the XML for that victory condition.
2.  **Using the Victory Message**:
    
    -   Instead of the hard-coded "beats" statement, the program now prints the victory message extracted from the XML, providing a more engaging and contextually relevant response.
#### `get_computer_action(user_actions_history)`

```python
def get_computer_action(user_actions_history):
```

- **Purpose**: Determines the computer’s action based on the user’s recent choices.
- **Logic**:
  - If there’s no user action history, it selects a random action.
  - Otherwise, it finds the user’s most frequent recent action and picks an action that can beat it (using `get_winner_action()`).

#### `get_user_action()`

```python
def get_user_action():
```

- **Purpose**: Collects the user’s action input from the console.
- **Logic**:
  - Displays available actions and prompts the user for their choice.
  - Validates the input, ensuring it’s within the valid range.

#### `get_random_computer_action()`

```python
def get_random_computer_action():
```

- **Purpose**: Randomly selects an action for the computer.
- **Logic**: Chooses a random action from the `GameAction` enum.

#### `get_winner_action(game_action)`

```python
def get_winner_action(game_action):
```

- **Purpose**: Finds an action that beats a given `game_action`.
- **Logic**: Searches the XML data for an action that wins against `game_action` and returns it.

#### `play_another_round()`

```python
def play_another_round():
```

- **Purpose**: Asks the user if they want to play another round.
- **Logic**: Returns `True` if the user responds with 'y', otherwise returns `False`.

#### `main()`

```python
def main():
```

- **Purpose**: Runs the main game loop.
- **Logic**:
  - Initializes lists to track the game’s results and the user’s action history.
  - Repeatedly:
    - Gets the user’s action.
    - Determines the computer’s action based on the user’s recent actions.
    - Assesses the game result.
    - Stores the result and prompts the user to play another round.

### Running the Game

To run the game, simply execute the script in a Python environment:

```bash
python rock_paper_scissors_lizard_spock.py
```

Each round, the user is prompted to choose an action. After evaluating the result, the user can decide whether to continue or stop.
