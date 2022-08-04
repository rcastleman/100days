from turtle import Turtle,Screen
import random 

screen = Screen()
screen.setup(width=500,height=400)
# speed("fastest")
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle? enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]

racers = []

def create_turtles():
    x = -230
    y = -100
    spacing = 40
    for color in colors:
        racer = Turtle(shape="turtle")
        racer.speed(0)
        racer.color(color)
        racer.penup()
        racer.setpos(x,y)
        racers.append(racer)
        y += spacing


create_turtles()

if user_bet:
    race_over = False
    while race_over == False:
        for racer in racers:
            racer.forward(random.randint(0,10))
            if racer.xcor() >= 100:
                race_over = True
                print(f"Race over!  {racer.color()} is the winner")
                if user_bet == racer.color:
                    print("You won!")
                else:
                    print("Sorry, you lost")

screen.exitonclick()
