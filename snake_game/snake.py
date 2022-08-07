from turtle import Screen,Turtle
import time

class Snake:

    def __init__(self,num_segments):
        self.x = 0
        self.y = 0
        self.spacing = 20
        self.num_segments = num_segments
        self.segments = []
        for i in range(self.num_segments):
            self.segment_i = Turtle("square")
            self.segment_i.color("white")
            self.segment_i.penup()
            self.segment_i.setpos(self.x,self.y)
            self.segments.append(self.segment_i)
            self.x -= self.spacing

    def move():
            """loops through all segments (no matter how many) starting from the LAST ... each segment goes to the position of the segment before it (ie last, next-to-last, etc.) thus following the first segment, no matter where it goes"""
            for segnum in range(len(snake.segments)-1,0,-1): 
                new_x = segments[segnum - 1].xcor()
                new_y = segments[segnum - 1].ycor()
                segments[segnum].goto(new_x,new_y)
            segments[0].forward(20)
            segments[0].left(90)
