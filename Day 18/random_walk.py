import random
import turtle as t
t.colormode(255)

screen = t.Screen()
timmy = t.Turtle()
timmy.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)
 
# colors = ["gray","blue","red","green","black","brown","orange","chartreuse","hot pink","dark violet"]
angles = [0,90,270]

for _ in range(100):
    timmy.color(random_color())
    timmy.width(10)
    timmy.speed(10)
    timmy.forward(30)
    timmy.right(random.choice(angles))

screen.exitonclick()