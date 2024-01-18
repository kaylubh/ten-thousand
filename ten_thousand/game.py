def get_input(*valid_input):
    """
    
    """

    response = input("> ")
    response = response.lower()

    # check response for valid input
    if response in valid_input:
        return response
    else:
        print("Invalid input. Enter a character in () from above.")
        get_input(*valid_input)

def welcome():
    """
    
    """

    welcome_message = "Welcome to Ten Thousand"
    play_prompt = "(y)es to play or (n)o to decline"

    print(welcome_message)
    print(play_prompt)

    response = get_input("y", "n")

    if response == "y":
        pass
    elif response == "n":
        print("OK. Maybe another time")

def play():
    welcome()


################
## Start Game ##
################

if __name__ == "__main__":
    play()
