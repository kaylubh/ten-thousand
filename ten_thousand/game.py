from ten_thousand.game_logic import GameLogic

def get_input(*valid_input, dice_input = False):
    """
    Gets input from the user then validates, formats, and returns the input.

    Parameters:
    *valid_input (strings): a variable number of valid user inputs to check against, will prompt user for input until their response matches a valid input
    dice_input (boolean)(default = False): if passed a True argument, validates and formats the user input using the dice input conditions instead of default

    Returns:
    string: user input
    """

    response = input("> ")
    response = response.lower()

    # handle dice input
    if dice_input:
        return response.replace(" ", "")

    # check response for valid input
    if response in valid_input:
        return response
    else:
        print("Invalid input. Enter a character in () from above.")
        get_input(*valid_input)

def roll_dice(num_dice):
    """
    Uses the GameLogic class to simulate rolling a given number of dice.

    Parameters:
    num_dice (integer): the number of dice to roll

    Returns:
    string: formatted string representing the rolled dice
    """

    rolled_dice = GameLogic.roll_dice(num_dice)

    # formats rolled dice values into a string to be rendered
    rolled_dice_string = " ".join(str(_) for _ in rolled_dice)
    rolled_dice_display = f"*** {rolled_dice_string} ***"

    return rolled_dice_display

def get_score(dice_to_score_string):
    """
    Uses the GameLogic class to calculate the score from a given dice roll.

    Parameters:
    dice_to_score_string (string): a string of numbers representing the dice roll values to score

    Returns:
    integer: the calculated score from the input dice roll
    """

    # converts the input from a string to a tuple of integers
    dice_to_score_strings = list(dice_to_score_string)
    dice_to_score_integers = tuple(int(_) for _ in dice_to_score_strings)

    score = GameLogic.calculate_score(dice_to_score_integers)

    return score

def game_session():
    """
    Logic for running a game session. Manages the turns, score-keeping, and completion of a game.
    """

    round = 1
    dice = 6
    total_score = 0
    round_score = 0
    continue_game = True

    while continue_game:
        # begin round
        print(f"Starting round {round}")
        print(f"Rolling {dice} dice...")
        print(roll_dice(dice))
        print("Enter dice to keep, or (q)uit:")

        # prompt user to score dice for current turn or quit
        response = get_input(dice_input = True)
        
        # quit game
        if response == "q":
            print(f"Thanks for playing. You earned {total_score} points")

            continue_game = False

        # score user selected dice
        else:
            round_score += get_score(response)
            dice -= len(response)

            print(f"You have {round_score} unbanked points and {dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            
            # prompt user to take another turn, bank score and begin new round, or quit game
            continue_response = get_input("r", "b", "q")

            # take another turn
            if continue_response == "r":
                pass # TODO
            
            # bank current score and begin next round
            elif continue_response == "b":
                total_score += round_score

                print(f"You banked {round_score} points in round {round}")
                print(f"Total score is {total_score} points")

                round += 1
                dice = 6
                round_score = 0
            
            # quit game
            elif continue_response == "q":
                print(f"Thanks for playing. You earned {total_score} points")

                continue_game = False

def play():
    """
    Begins the game on run. Depending on user input, begins a game session or exits the program.
    """

    welcome_message = "Welcome to Ten Thousand"
    play_prompt = "(y)es to play or (n)o to decline"

    print(welcome_message)
    print(play_prompt)

    # prompt user to begin a game session or quit the game
    response = get_input("y", "n")

    if response == "y":
        game_session()
    elif response == "n":
        print("OK. Maybe another time")


################
## Start Game ##
################

if __name__ == "__main__":
    play()
