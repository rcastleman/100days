from cgitb import reset
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# MOVE_DISTANCE = 20

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move_right()
    screen.update()
    #detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()
    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.move_left()
    #detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.move_right()

screen.exitonclick()