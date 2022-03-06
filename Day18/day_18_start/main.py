import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
turtle.colormode(255)
# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)

# for _ in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

#


def ran():
    color1 = random.randint(1, 255)
    color2 = random.randint(1, 255)
    color3 = random.randint(1, 255)
    tup = (color1, color2, color3)
    return tup


# colors = ["aqua", "bisque", "blue violet", "chartreuse", "red", "pink", "green", "purple"]
# directions = [0, 90, 180, 270]
timmy.speed(15)
# timmy.pensize(10)
# for _ in range(150):
#     timmy.color(ran())
#     timmy.left(random.choice(directions))
#     timmy.forward(40)


# for n in range(3, 11):
#     degree = 360 / n
#     timmy.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
#     for i in range(n):
#         timmy.forward(100)
#         timmy.right(degree)
angle = 5
times = int(360/angle)
for _ in range(times):
    timmy.color(ran())
    timmy.circle(100)
    timmy.right(angle)

screen = Screen()
screen.colormode(255)

screen.exitonclick()
