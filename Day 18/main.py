from turtle import Turtle,Screen

screen = Screen()

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen.exitonclick()