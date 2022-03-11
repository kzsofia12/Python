from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.penup()
        self.setpos(position_x, position_y)

    def move_up(self):
        x = self.xcor()
        y = self.ycor() + 20
        if 260 > y:
            self.goto(x, y)

    def move_down(self):
        x = self.xcor()
        y = self.ycor() - 20
        if -260 < y:
            self.goto(x, y)
