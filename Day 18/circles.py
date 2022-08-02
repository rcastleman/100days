import random
import turtle as t
t.colormode(255)

screen = t.Screen()

# circle = t.Shape()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)
 

t.speed("fastest")

def spirograph(shift):
    for i in range(int(360/shift)):
        t.circle(100)
        t.color(random_color())
        t.setheading(t.heading() + shift)

spirograph(5)

screen.exitonclick()