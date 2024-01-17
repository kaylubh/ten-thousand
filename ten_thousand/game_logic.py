import random
from collections import Counter

class GameLogic:
    """
    The game logic for a game of ten thousand. Methods assume the game is being played with a standard D6 and that no more than 6 dice are being rolled per round.

    Methods:
    calculate_score(rolls): Calculates the score according to the rules of the game from a given collection of rolls. Returns an integer of the highest total score from the input rolls.
    roll_dice(num_dice): Simulates "rolling" a number of dice equal to the input num_dice and returns a tuple of the values of the "rolls".
    """

    @staticmethod
    def calculate_score(rolls):
        """
        calculate_score(rolls): Calculates the score according to the rules of the game from a given collection of rolls. Returns an integer of the highest total score from the input rolls.

        Parameters:
        `rolls` (collection of integers): The values of rolled dice to be scored.

        Returns:
        integer: The highest possible score from the input rolls.
        """
        totaled_rolls_counts = Counter(rolls) # Counter({value: rolls, value: rolls})
        sorted_rolls_counts = totaled_rolls_counts.most_common() # [(value, rolls), (value, rolls)] sorted

        score = 0

        for roll_count in sorted_rolls_counts:
            value = roll_count[0]
            count = roll_count[1]

            # all 1's
            if value == 1:
                if count < 3:
                    score += 100 * count
                else:
                    multiplier = 1000 * (count - 3)
                    score += 1000 + multiplier

            # 1-2 count of 5's
            if value == 5:
                if count < 3:
                    score += 50 * count

            # three-six of a kind excluding 1's        
            if value != 1:
                if count >= 3:
                    three_of_a_kind_score = value * 100
                    multiplier = three_of_a_kind_score * (count - 3)
                    score += three_of_a_kind_score + multiplier

        # full house
        if len(sorted_rolls_counts) == 6:
            score = 1500

        # three pairs
        if len(sorted_rolls_counts) == 3:
            if sorted_rolls_counts[0][1] == 2 and sorted_rolls_counts[1][1] == 2:
                score = 1500

        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        roll_dice(num_dice): Simulates "rolling" a number of dice equal to the input num_dice and returns a tuple of the values of the "rolls".

        Parameters:
        `num_dice` (integer): The number of dice to be "rolled".

        Returns:
        tuple: The values of the "rolled" dice.
        """
        return tuple(random.randint(1, 6) for _ in range(num_dice))
