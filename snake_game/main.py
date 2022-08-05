from turtle import Screen,Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x = 0
y = 0
spacing = 20

for i in range(3):
    segment_i = Turtle("square")
    segment_i.color("white")
    segment_i.setpos(x,y)
    x -= spacing

screen.exitonclick()