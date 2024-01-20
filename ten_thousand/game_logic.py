import random
from collections import Counter

class GameLogic:
    """
    The game logic for a game of ten thousand. Methods assume the game is being played with a standard D6 and that no more than 6 dice are being rolled per round.

    Methods:
    calculate_score(rolls): Calculates the score according to the rules of the game from a given collection of rolls. Returns an integer of the highest total score from the input rolls.
    roll_dice(num_dice): Simulates "rolling" a number of dice equal to the input num_dice and returns a tuple of the values of the "rolls".
    get_scorers(rolls): Given a collection of roll values, returns the rolls which would qualify to be scored per the rules of the game.
    validate_keepers(rolls, selected_rolls): Given a collection of roll values and a collection of selected rolls, checks if the selection is a legal selection in the game.
    """

    @staticmethod
    def calculate_score(rolls):
        """
        calculate_score(rolls): Calculates the score according to the rules of the game from a given collection of rolls. Returns an integer of the highest total score from the input rolls.

        Parameters:
        rolls (collection of integers): values of rolled dice to be scored

        Returns:
        integer: highest possible score from the input rolls
        """

        totaled_rolls_counts = Counter(rolls) # Counter({value: count, value: count})
        sorted_rolls_counts = totaled_rolls_counts.most_common() # [(value, count), (value, count)] sorted

        score = 0

        for roll_count in sorted_rolls_counts:
            value = roll_count[0] # value of the dice (1, 2, 3, 4, 5, 6)
            count = roll_count[1] # count of times the value was rolled

            # scores all "1" values
            if value == 1:
                if count < 3:
                    score += 100 * count
                else:
                    multiplier = 1000 * (count - 3)
                    score += 1000 + multiplier

            # scores "5" values if count is 1 or 2
            if value == 5 and count < 3:
                    score += 50 * count

            # scores all values except "1" for three, four, five, or six of a kind      
            if value != 1 and count >= 3:
                    three_of_a_kind_score = value * 100
                    multiplier = three_of_a_kind_score * (count - 3)
                    score += three_of_a_kind_score + multiplier

        # scores a full house
        if len(sorted_rolls_counts) == 6: # six unique values rolled must be full house
            score = 1500

        # scores three pairs
        if len(sorted_rolls_counts) == 3: # three unique values rolled
            if sorted_rolls_counts[0][1] == 2 and sorted_rolls_counts[1][1] == 2: # all are pairs
                score = 1500

        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        roll_dice(num_dice): Simulates rolling a number of dice equal to the input num_dice and returns a tuple of the values of the "rolls".

        Parameters:
        num_dice (integer): number of dice to be rolled

        Returns:
        tuple: values of the rolled dice
        """

        return tuple(random.randint(1, 6) for _ in range(num_dice))
    
    @staticmethod
    def get_scorers(rolls):
        """
        get_scorers(rolls): Given a collection of roll values, returns the rolls which would qualify to be scored per the rules of the game.

        Parameters:
        rolls (collection of integers): values of rolled dice to evaluate for scoring eligibility

        Returns:
        tuple: values of rolled dice which would be eligible to be scored
        """

        totaled_rolls_counts = Counter(rolls) # Counter({value: count, value: count})
        sorted_rolls_counts = totaled_rolls_counts.most_common() # [(value, count), (value, count)] sorted

        # check for full house
        if len(sorted_rolls_counts) == 6: # six unique values rolled must be full house
            return rolls

        # check for three pairs
        if len(sorted_rolls_counts) == 3: # three unique values rolled
             if sorted_rolls_counts[0][1] == 2 and sorted_rolls_counts[1][1] == 2: # all are pairs
                  return rolls

        scorers = []

        # add "1" to scorers
        scorers += [roll for roll in rolls if roll == 1]

        # add "5" to scorers
        scorers += [roll for roll in rolls if roll == 5]

        # add three, four, five, or six of a kind scorers
        for roll_count in sorted_rolls_counts:
            value = roll_count[0] # value of the dice (1, 2, 3, 4, 5, 6)
            count = roll_count[1] # count of times the value was rolled

            if value != 1 and value != 5 and count >= 3:
                scorers += [roll for roll in rolls if roll == value]

        return tuple(scorers)

    @staticmethod
    def validate_keepers(rolls, selected_rolls):
        """
        validate_keepers(rolls, selected_rolls): Given a collection of roll values and a collection of selected rolls, checks if the selection is a legal selection in the game.

        Parameters:
        rolls (collection of integers): values of rolled dice to compare the selected rolls against
        selected_rolls (collection of integers): values of selected rolls to be compared against the actual rolls for legality with the rules

        Returns:
        boolean: True if a legal selection, False if an illegal selection      
        """

        legal_selection = True

        # compare roll values to the selected dice for legal selections
        roll_counts = Counter(rolls) # Counter({value: count, value: count})
        selected_counts = Counter(selected_rolls)
        
        for selected in selected_counts:
            # selected dice value is in the roll
            legal_selection = selected in roll_counts

            # run this check only if first test passes
            if legal_selection:
                # the number of a value of selected dice is <= the number of a value in the roll
                legal_selection = selected_counts[selected] <= roll_counts[selected]

        return legal_selection
