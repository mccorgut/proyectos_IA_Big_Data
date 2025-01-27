import random
from enum import IntEnum
from statistics import mode
from xml.etree import ElementTree

# Load the XML file containing victory conditions
Victories = ElementTree.parse('victories.xml').getroot()


# Enum for different game actions
class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


# Enum for game results
class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


# Number of recent actions to consider for the computer's choice
NUMBER_RECENT_ACTIONS = 5


# Assess the outcome of the game based on user and computer actions
def assess_game(user_action, computer_action):
    # Check if it's a tie
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return GameResult.Tie

    # Check for victory conditions
    for victory in Victories.iter('victory'):
        # Check if user wins
        if (user_action.name == victory.attrib['choice'] and
                computer_action.name == victory.attrib['against']):
            print(f"You won! {user_action.name} beats {computer_action.name}.")
            return GameResult.Victory
        # Check if computer wins
        if (computer_action.name == victory.attrib['choice'] and
                user_action.name == victory.attrib['against']):
            print(f"You lost! {computer_action.name} beats {user_action.name}.")
            return GameResult.Defeat


# Determine the computer's action based on user actions history
def get_computer_action(user_actions_history):
    # No previous user actions => random computer choice
    if not user_actions_history:
        computer_action = get_random_computer_action()
    else:
        # Determine the most frequent recent action by the user
        most_frequent_recent_action = GameAction(mode(user_actions_history[-NUMBER_RECENT_ACTIONS:]))
        # Get the winning action against the user's most frequent action
        computer_action = get_winner_action(most_frequent_recent_action)

    # Show the computer's choice
    print(f"Computer picked {computer_action.name}.")
    return computer_action


# Get the user's action input
def get_user_action():
    # Prepare the string for displaying available choices
    game_choices = list(GameAction)
    game_choices_str = ", ".join(f"{game_action.name}[{game_action.value}]" for game_action in game_choices)

    while True:
        try:
            # Prompt the user for their choice
            user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
            # Validate user input
            if user_selection < 0 or user_selection >= len(GameAction):
                raise ValueError("Selection out of range.")
            return GameAction(user_selection)
        except ValueError as e:
            print(f"Invalid selection. {str(e)} Pick a choice in range [0, {len(GameAction) - 1}]!")


# Generate a random action for the computer
def get_random_computer_action():
    return GameAction(random.randint(0, len(GameAction) - 1))


# Get a winning action against the provided game action
def get_winner_action(game_action):
    # Iterate through the victories to find the winning action
    for victory in Victories.iter('victory'):
        if victory.attrib['choice'] == game_action.name:
            return GameAction[victory.attrib['against']]
    return None


# Ask the user if they want to play another roundA
def play_another_round():
    return input("\nAnother round? (y/n): ").lower() == 'y'


# Main function to run the game
def main():
    game_history = []  # To track the results of each game
    user_actions_history = []  # To track the user's actions

    while True:
        user_action = get_user_action()  # Get the user's action
        user_actions_history.append(user_action)  # Save user action history

        computer_action = get_computer_action(user_actions_history)  # Get the computer's action
        game_result = assess_game(user_action, computer_action)  # Assess the game result
        game_history.append(game_result)  # Save the game result history

        # Ask the user if they want to play another round
        if not play_another_round():
            break  # Exit the loop if the user doesn't want to continue


if __name__ == "__main__":
    main()
