import random
from collections import Counter

class GameLogic:

    @staticmethod
    def calculate_score(rolls):
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

            # 3-6 of a kind excluding 1's        
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
        return tuple(random.randint(1, 6) for _ in range(num_dice))
