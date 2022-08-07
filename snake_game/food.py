from turtle import Turtle,Screen
import random

# needs to go to a random coordinate
# if the snake hits it, it moves to a new random coordinate

class Food:
    def __init__(self):
        super().__init__():
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto()


