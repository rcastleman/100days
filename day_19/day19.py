from turtle import Turtle,Screen

from numpy import spacing

screen = Screen()
screen.setup(width=500,height=400)
# user_bet = screen.textinput(title="Make your bet",prompt="Which turtle? enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]

def create_turtles():
    x = -230
    y = -100
    spacing = 40
    for color in colors:
        racer = Turtle(shape="turtle")
        racer.color(color)
        racer.penup()
        racer.setpos(x,y)
        y += spacing

create_turtles()

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230,y =-100)


screen.exitonclick()
