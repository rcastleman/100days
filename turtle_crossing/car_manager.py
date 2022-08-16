from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

last_position = (280,0)

class CarManager(Turtle):
    

    def __init__(self):
        global last_position
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.color(random.choice(COLORS))
        #initializes car at x = 280 and a random y outside of the safe zones 
        self.postition = (280,random.randint(-250,250))
        last_position = self.position
