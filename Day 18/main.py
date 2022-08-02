from turtle import Turtle,Screen, color, pencolor
import random

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
# timmy.color("blue")
# 
colors = ["gray","blue","red","green","black","brown","orange","chartreuse","hot pink","dark violet"]

def draw_shape(sides,angle):
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for sides in range(3,11):
    timmy.color(random.choice(colors))
    timmy.width(10)
    angle = 360 / sides
    draw_shape(sides,angle)

# for _ in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

screen.exitonclick()