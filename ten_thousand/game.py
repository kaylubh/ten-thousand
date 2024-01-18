from ten_thousand.game_logic import GameLogic

def get_input(*valid_input, dice_input = False):
    """
    
    """

    response = input("> ")
    response = response.lower()

    # handle dice input
    if dice_input:
        return response

    # check response for valid input
    if response in valid_input:
        return response
    else:
        print("Invalid input. Enter a character in () from above.")
        get_input(*valid_input)

def roll_dice(num_dice):
    """
    
    """

    rolled_dice = GameLogic.roll_dice(num_dice)

    rolled_dice_string = " ".join(str(_) for _ in rolled_dice)
    rolled_dice_display = f"*** {rolled_dice_string} ***"

    return rolled_dice_display

def game_session():
    """
    
    """

    round = 0
    dice = 6
    total_score = 0

    print(f"Starting round {round}")
    print(f"Rolling {dice} dice...")
    print(roll_dice(dice))
    print("Enter dice to keep, or (q)uit:")

    response = get_input(dice_input = True)
    
    if response == "q":
        print(f"Thanks for playing. You earned {total_score} points")
    else:
        pass

def welcome():
    """
    
    """

    welcome_message = "Welcome to Ten Thousand"
    play_prompt = "(y)es to play or (n)o to decline"

    print(welcome_message)
    print(play_prompt)

    response = get_input("y", "n")

    if response == "y":
        game_session()
    elif response == "n":
        print("OK. Maybe another time")

def play():
    welcome()


################
## Start Game ##
################

if __name__ == "__main__":
    play()
