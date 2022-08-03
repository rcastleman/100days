import random
import turtle
turtle.colormode(255)
screen = turtle.Screen()

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

a = turtle.Turtle()
a.shape("circle")
a.color("white",random.choice(color_list))

def set_start_position():
    """create turtle and put in position"""
    a.hideturtle()         
    a.penup()              
    a.goto(-200, -200)     

def draw_row():
    """draw ten dots horizontally using a random color for each"""
    for _ in range(9):
        a.showturtle()
        a.color("white",random.choice(color_list))
        a.stamp()
        a.forward(50)

def move_up_left():
    """move pen up one row to commence another row"""
    a.left(90)
    a.stamp()
    a.forward(50)
    a.left(90)

def move_up_right():
    """move pen up one row to commence another row"""
    a.right(90)
    a.stamp()
    a.forward(50)
    a.right(90)

def sequence():
    """draw a 10 x 10 array of Hirst dots with random colors"""
    set_start_position()
    for i in range(9):
        draw_row()
        if i % 2 == 0:
            move_up_left()
        if i % 2 == 1:
            move_up_right()
        draw_row()

sequence()

screen.exitonclick()