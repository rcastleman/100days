from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

#screen setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # print(f"Segment length: {len(snake.segments)}")
        scoreboard.increase_score()
    
    #detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    
    #detect tail collisions - if head collides with any segment of the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 2:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()