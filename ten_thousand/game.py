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
        # quit game
        if response == "q":
            return response
        
        # dice input
        else:
            # removes spaces
            response = response.replace(" ", "")

            # converts the input from a string to a tuple of integers
            dice_to_score_strings = list(response)
            dice_to_score_integers = tuple(int(_) for _ in dice_to_score_strings)

            return dice_to_score_integers

    # check response for valid input
    if response in valid_input:
        return response
    else:
        print("Invalid input. Enter a character in () from above.")
        get_input(*valid_input)

def roll_dice(num_dice, roller):
    """
    Uses the GameLogic class to simulate rolling a given number of dice.

    Parameters:
    num_dice (integer): the number of dice to roll

    Returns:
    string: formatted string representing the rolled dice
    """

    # roll the dice or use simulated rolls for tests
    roll_engine = roller or GameLogic.roll_dice
    rolled_dice = roll_engine(num_dice)

    # formats rolled dice values into a string to be rendered
    rolled_dice_string = " ".join(str(_) for _ in rolled_dice)
    rolled_dice_display = f"*** {rolled_dice_string} ***"

    return rolled_dice, rolled_dice_display

def get_score(dice_to_score):
    """
    Uses the GameLogic class to calculate the score from a given dice roll.

    Parameters:
    dice_to_score_string (string): a string of numbers representing the dice roll values to score

    Returns:
    integer: the calculated score from the input dice roll
    """

    score = GameLogic.calculate_score(dice_to_score)

    return score

def game_turn(num_dice, roller):
    """
    
    """

    # roll dice
    rolls, rolls_string = roll_dice(num_dice, roller)

    print(f"Rolling {num_dice} dice...")
    print(rolls_string)

    # prompt user to score dice for current turn or quit
    print("Enter dice to keep, or (q)uit:")
    response = get_input(rolls, dice_input = True)

    return response

def game_round(round, roller):
    """
    
    """

    num_dice = 6
    round_score = 0
    continue_round = True

    # begin round
    print(f"Starting round {round}")

    while continue_round:

        turn_response = game_turn(num_dice, roller)

        # quit game
        if turn_response == "q":
            return "q"
        
        # score user selected dice
        else:
            round_score += get_score(turn_response)
            num_dice -= len(turn_response)

            # check for hot dice
            if num_dice == 0:
                num_dice = 6

            print(f"You have {round_score} unbanked points and {num_dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            
            # prompt user to take another turn, bank score and begin new round, or quit game
            continue_response = get_input("r", "b", "q")

            # take another turn
            if continue_response == "r":
                pass

            # bank score
            if continue_response == "b":
                return "b", round_score
            
            # quit game
            if continue_response == "q":
                return "q"

def game_session(roller):
    """
    Logic for running a game session. Manages the turns, score-keeping, and completion of a game.
    """

    round = 1
    total_score = 0
    continue_game = True

    while continue_game:

        round_response = game_round(round, roller)
            
        # bank current score and begin next round
        if round_response[0] == "b":
            round_score = round_response[1]
            total_score += round_score

            print(f"You banked {round_score} points in round {round}")
            print(f"Total score is {total_score} points")

            round += 1
            
        # quit game
        elif round_response[0] == "q":
            print(f"Thanks for playing. You earned {total_score} points")

            continue_game = False

def play(roller = None):
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
        game_session(roller)
    elif response == "n":
        print("OK. Maybe another time")


################
## Start Game ##
################

if __name__ == "__main__":
    play()
