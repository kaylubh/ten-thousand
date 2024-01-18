def welcome():
    welcome_message = "Welcome to Ten Thousand \n Enter 'q' at any time to exit"
    play_prompt = "(y)es to play or (n)o to decline"

    print(welcome_message)
    print(play_prompt)

    response = get_input()

    if response == "y":
        pass
    elif response == "n":
        print("OK. Maybe another time")

def play():
    pass


################
## Start Game ##
################

if __name__ == "__main__":
    play()
