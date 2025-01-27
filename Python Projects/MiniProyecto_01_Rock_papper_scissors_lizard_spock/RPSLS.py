import random
from enum import IntEnum
from statistics import mode
from xml.etree import ElementTree

# Load the XML file containing the victory conditions
Victories = ElementTree.parse('victories.xml').getroot()
print(type(Victories))


# Enum for different game actions (Rock, Paper, Scissors, Lizard, Spock)
class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


# Enum for possible game outcomes
class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


# Number of recent actions to consider when predicting user's choice
NUMBER_RECENT_ACTIONS = 5


# Determine the game result based on user and computer actions by checking XML conditions
def assess_game(user_action, computer_action):
    # Check if it’s a tie
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return GameResult.Tie

    # Check if the user wins by looking up the conditions in XML
    victory_path = f"./victory[@choice='{user_action.name}'][@against='{computer_action.name}']"
    victory_element = Victories.find(victory_path)

    if victory_element is not None:
        victory_message = victory_element.text.strip()  # Get the text and strip any whitespace
        print(f"You won! {victory_message}")
        return GameResult.Victory

    # If it's not a tie or a user win, then the computer wins
    defeat_message = f"{computer_action.name} beats {user_action.name}."  # Default defeat message
    print(f"You lost! {defeat_message}")
    return GameResult.Defeat


# Determine the computer's next action based on the user's action history
def get_computer_action(user_actions_history):
    # If no history, choose randomly
    if not user_actions_history:
        computer_action = get_random_computer_action()
    else:
        # Get the user's most common recent action
        most_frequent_recent_action = GameAction(mode(user_actions_history[-NUMBER_RECENT_ACTIONS:]))
        # Determine the winning action against the user's most frequent recent action
        computer_action = get_winner_action(most_frequent_recent_action)

    # Print the computer's chosen action
    print(f"Computer picked {computer_action.name}.")
    return computer_action


# Get the user's action as input from the console
def get_user_action():
    # Prepare a list of choices for display
    game_choices = list(GameAction)
    game_choices_str = ", ".join(f"{game_action.name}[{game_action.value}]" for game_action in game_choices)

    while True:
        try:
            # Prompt user for their choice and convert to integer
            user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
            # Validate the user input
            if user_selection < 0 or user_selection >= len(GameAction):
                raise ValueError("Selection out of range.")
            return GameAction(user_selection)
        except ValueError as e:
            print(f"Invalid selection. {str(e)} Pick a choice in range [0, {len(GameAction) - 1}]!")


# Generate a random action for the computer
def get_random_computer_action():
    return GameAction(random.randint(0, len(GameAction) - 1))


# Get an action that beats the provided game action based on XML victory conditions
def get_winner_action(game_action):
    # Find the winning action by searching in the XML data
    for victory in Victories.iter('victory'):
        if victory.attrib['choice'] == game_action.name:
            return GameAction[victory.attrib['against']]
    return None  # Return None if no winning action is found


# Ask the user if they want to play another round of the game
def play_another_round():
    return input("\nAnother round? (y/n): ").lower() == 'y'


# Main function to run the game loop
def main():
    game_history = []  # Tracks the outcomes of each game round
    user_actions_history = []  # Tracks the user's chosen actions

    while True:
        user_action = get_user_action()  # Get the user's chosen action
        user_actions_history.append(user_action)  # Add to history

        computer_action = get_computer_action(user_actions_history)  # Determine computer's action
        game_result = assess_game(user_action, computer_action)  # Evaluate the outcome
        game_history.append(game_result)  # Store the game outcome

        # Ask if the user wants to play again
        if not play_another_round():
            break  # Exit loop if user does not wish to continue


# Run the main function if this script is executed
if __name__ == "__main__":
    main()
