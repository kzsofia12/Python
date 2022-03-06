from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
head = timmy.heading()
timmy.shape("turtle")


def move_forwards():
    timmy.forward(15)


def move_back():
    timmy.backward(15)


def counter_clock():
    timmy.setheading(timmy.heading() + 10)


def clock():
    timmy.setheading(timmy.heading() - 10)


def re():
    timmy.reset()
    timmy.clear()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_back, "s")
screen.onkey(counter_clock, "a")
screen.onkey(clock, "d")
screen.onkey(re, "c")

screen.exitonclick()
