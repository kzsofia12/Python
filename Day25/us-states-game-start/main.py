import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

timmy = turtle.Turtle()

data = pandas.read_csv("50_states.csv")
timmy.hideturtle()
game_is_on = True
correct_answers = []
all_state = data.state.to_list()
missing_state = []

while game_is_on:
    answer_stat = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another sta"
                                                                                             "te's name?").title()


    if answer_stat == "Exit":
        game_is_on = False
        for state in all_state:
            if state not in correct_answers:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")

    elif answer_stat in all_state:
        if answer_stat not in correct_answers:
            ok_data = data[data.state == answer_stat]
            timmy.penup()
            x = int(ok_data.x)
            y = int(ok_data.y)
            timmy.goto(x, y)
            timmy.pendown()
            timmy.write(answer_stat, False, font=("arial", 7, "normal"))
            correct_answers.append(answer_stat)

    elif len(correct_answers) == 50:
        game_is_on = False

screen.exitonclick()
