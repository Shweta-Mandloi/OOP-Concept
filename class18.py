# 18. Dice — Roll and Show Value

import random

class Dice:
    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

    def show(self):
        print("Rolled:", self.value)

dice = Dice()
dice.roll()
dice.show()
