from turtle import Screen,Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.exitonclick()

def create_snake():
    # for _ in range(3):
    snake = Turtle(shape="square")
    snake.color("white")
    # snake.shapesize(20,20)
    # snake.xcor -= 10

create_snake()
    
