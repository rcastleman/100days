
from turtle import Turtle

class Paddle:
    
    def __init__(self) -> None:
        pass
        
    def create_paddle(self,x_cor,y_cor):
        self.xcor = x_cor
        self.ycor = y_cor
        self.width = 20
        self.height = 100
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x_cor,y_cor)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

    screen.listen()
    screen.onkey(go_up,"Up")
    screen.onkey(go_down,"Down")
