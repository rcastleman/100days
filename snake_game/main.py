from turtle import Screen,Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# screen.tracer(0)

x = 0
y = 0
spacing = 20

segments = []

for i in range(3):
    segment_i = Turtle("square")
    segment_i.penup()
    segment_i.color("white")
    segment_i.setpos(x,y)
    segments.append(segment_i)
    x -= spacing

# screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #loop through all segments (no matter how many) starting from the LAST ... each segment goes 
    #to the position of the segment before it (ie last, next-to-last, etc.) thus "following" the 
    #first segment, no matter where it goes
    for segnum in range(len(segments)-1,0,-1): 
        new_x = segments[segnum - 1].xcor()
        new_y = segments[segnum - 1].ycor()
        segments[segnum].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()