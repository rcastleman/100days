from turtle import Screen,Turtle
import time

class Snake():

    def __init__(self,initial_segments):
        self.initial_segments = initial_segments
    
    def create_snake():
        x = 0
        y = 0
        spacing = 20
        segments = []
        for i in range(self.initial_segments):
            segment_i = Turtle("square")
            segment_i.color("white")
            segment_i.penup()
            segment_i.setpos(x,y)
            segments.append(segment_i)
            x -= spacing

    def move():
            """loops through all segments (no matter how many) starting from the LAST ... each segment goes to the position of the segment before it (ie last, next-to-last, etc.) thus following the first segment, no matter where it goes"""
            for segnum in range(len(snake.segments)-1,0,-1): 
                new_x = segments[segnum - 1].xcor()
                new_y = segments[segnum - 1].ycor()
                segments[segnum].goto(new_x,new_y)
            segments[0].forward(20)
            segments[0].left(90)
