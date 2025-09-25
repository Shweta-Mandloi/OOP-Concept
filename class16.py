# 16. Player — Level Up

class Player:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to {self.level}!")

player = Player("Zoe")
player.level_up()


