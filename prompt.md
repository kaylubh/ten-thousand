# Prompts

## Game Logic

Used GitHub Copilot as the AI tool to create starter code.

### Prompt

Using the following instructions and the tests located in the tests folder as a guide. Create a simple Python program that implements the requirements below which will be used to create the game logic for an application that allows a user to play a game of ten thousand. All the code should be in the defined class and should not create any additional features not outlined in the instructions. The code provided should pass all the tests.

Define a GameLogic class in ten_thousand/game_logic.py file.
Handle calculating score for dice roll
Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.
Handle rolling dice
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

### Response Code

```python
import random

class GameLogic:
    @staticmethod
    def calculate_score(roll):
        score = 0
        counts = [0] * 7
        for die in roll:
            counts[die] += 1

        # Calculate score for each die value
        for i in range(1, 7):
            count = counts[i]
            if count >= 3:
                if i == 1:
                    score += 1000
                else:
                    score += i * 100
                count -= 3

            if i == 1:
                score += count * 100
            elif i == 5:
                score += count * 50

        return score

    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))
```
