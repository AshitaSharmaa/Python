from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def score_update(self):
        self.clear()
        self.goto(-50, 250)
        self.write(self.l_score, align="center", font=("Courier", 50, "bold"))
        self.goto(50, 250)
        self.write(self.r_score, align="center", font=("Courier", 50, "bold"))

    def increase_score_l(self):
        self.l_score += 1
        self.score_update()

    def increase_score_r(self):
        self.r_score += 1
        self.score_update()
