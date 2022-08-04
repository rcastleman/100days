from turtle import Turtle,Screen
import random 

screen = Screen()
screen.setup(width=500,height=400)
# user_bet = screen.textinput(title="Make your bet",prompt="Which turtle? enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]

racers = []


def create_turtles():
    x = -230
    y = -100
    spacing = 40
    for color in colors:
        racer = Turtle(shape="turtle")
        racer.color(color)
        racer.penup()
        racer.setpos(x,y)
        racers.append(racer)
        y += spacing

def advance(racer):
    amount = random.randint(0,25)
    racer.forward(amount)


race_not_over = True
while race_not_over:
    for racer in racers:
        advance(racer)
        if racer.xcor == 250:
            print(f"Race over!  {racer} is the winner")
            race_not_over = False

create_turtles()

screen.exitonclick()
