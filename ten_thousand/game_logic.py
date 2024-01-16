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
