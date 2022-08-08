from turtle import Screen
import paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.exitonclick()

screen.listen()
screen.onkey(paddle.paddle_up,"Up")
screen.onkey(paddle.paddle_down,"Down")

