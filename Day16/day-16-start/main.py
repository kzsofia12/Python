# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen = turtle.Screen()
# my_screen.canvheight
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
print(table)
