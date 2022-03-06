from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
all_turtles = []

yn = -60
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=yn)
    all_turtles.append(new_turtle)
    yn += 30

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You win! The winning turtle is the {winning_color}")
            else:
                print(f"You lost! The winning turtle is the {winning_color}")
            is_race_on = False
        ran = random.randint(0, 10)
        turtle.forward(ran)


screen.exitonclick()
