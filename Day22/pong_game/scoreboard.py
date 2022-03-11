from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(-100, 200)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_right_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

