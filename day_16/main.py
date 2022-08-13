# from turtle import Turtle,Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# print(timmy)
# timmy.forward(100)

# my_screen = Screen()
# # print(my_screen.canvheight)
# print(my_screen.exitonclick())

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"],align="r")
table.add_column("Type",["Electric","Water","Fire"],align='r')
table.align = "l"
print(table)