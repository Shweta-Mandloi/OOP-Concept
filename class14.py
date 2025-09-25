# 14. ScoreBoard — Track and Display Score

class ScoreBoard:
    def __init__(self):
        self.score = 0

    def update_score(self, points):
        self.score += points

    def display_score(self):
        print("Current Score:", self.score)

sb = ScoreBoard()
sb.update_score(10)
sb.update_score(5)
sb.display_score()


