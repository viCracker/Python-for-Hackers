import random


class Dice:
    def roll(self):
        a = random.randint(1,6)
        b = random.randint(1,6)
        results = (a, b)
        return results


play1 = Dice()
print(play1.roll())
