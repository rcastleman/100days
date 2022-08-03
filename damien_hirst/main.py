import random
import turtle
turtle.colormode(255)
screen = turtle.Screen()

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

color = random.choice(color_list)

a = turtle.Turtle()
a.shape("circle")
a.color(color)    

def set_start_position():
    """create turtle and put in position"""
    a.hideturtle()         
    a.penup()              
    a.goto(-200, -200)     


def draw_row():
    """draw ten dots horizontally using a random color for each"""
    for width in range(9):
        a.showturtle()
        a.fillcolor(random.choice(color_list))
        a.stamp()
        a.forward(50)

def move_up():
    """move pen up one row to commence another row"""
    a.left(90)
    a.stamp()
    a.forward(50)
    a.left(90)

set_start_position()
draw_row()
move_up()
draw_row()

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)




screen.exitonclick()