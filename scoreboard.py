from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ["Arial", 12, "bold"])

    def game_over(self):
        self.home()
        self.color("blue")
        self.write("GAME OVER", False, "center", ["Arial", 15, "bold"])

    def add_score(self):
        self.score += 1
