from turtle import Screen,Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# screen.tracer(0)

x = 0
y = 0
spacing = 20

segments = []

for i in range(3):
    segment_i = Turtle("square")
    segment_i.penup()
    segment_i.color("white")
    segment_i.setpos(x,y)
    segments.append(segment_i)
    x -= spacing

# screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)

screen.exitonclick()