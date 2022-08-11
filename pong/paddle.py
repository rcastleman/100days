
from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position) -> None:
        super().__init__()
        # self.xcor = x_cor
        # self.ycor = y_cor
        # self.width = 20
        # self.height = 100
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
