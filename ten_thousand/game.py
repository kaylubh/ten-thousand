from ten_thousand.game_logic import GameLogic

def get_input(*valid_input, dice_input = False):
    """
    
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
    
    """

    rolled_dice = GameLogic.roll_dice(num_dice)

    rolled_dice_string = " ".join(str(_) for _ in rolled_dice)
    rolled_dice_display = f"*** {rolled_dice_string} ***"

    return rolled_dice_display

def get_score(dice_to_score_string):
    """
    
    """

    dice_to_score_strings = list(dice_to_score_string)
    dice_to_score_integers = tuple(int(_) for _ in dice_to_score_strings)

    score = GameLogic.calculate_score(dice_to_score_integers)

    return score

def game_session():
    """
    
    """

    round = 1
    dice = 6
    total_score = 0
    round_score = 0
    continue_game = True

    while continue_game:
        print(f"Starting round {round}")
        print(f"Rolling {dice} dice...")
        print(roll_dice(dice))
        print("Enter dice to keep, or (q)uit:")

        response = get_input(dice_input = True)
        
        if response == "q":
            print(f"Thanks for playing. You earned {total_score} points")

            continue_game = False

        else:
            round_score += get_score(response)
            dice -= len(response)

            print(f"You have {round_score} unbanked points and {dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            
            continue_response = get_input("r", "b", "q")

            if continue_response == "r":
                pass
            elif continue_response == "b":
                total_score += round_score

                print(f"You banked {round_score} points in round {round}")
                print(f"Total score is {total_score} points")

                round += 1
                dice = 6
                round_score = 0
            elif continue_response == "q":
                print(f"Thanks for playing. You earned {total_score} points")

                continue_game = False

def play():
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


################
## Start Game ##
################

if __name__ == "__main__":
    play()
