from turtle import Screen,Turtle
import time

MOVE_DISTANCE = 20
INITIAL_NUM_SEGMENTS = 3

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        # self.num_segments = num_segments

    def create_snake(self):
        self.x = 0
        self.y = 0
        self.spacing = 20
        for i in range(INITIAL_NUM_SEGMENTS):
            self.segment_i = Turtle("square")
            self.segment_i.color("white")
            self.segment_i.penup()
            self.segment_i.setpos(self.x,self.y)
            self.segments.append(self.segment_i)
            self.x -= self.spacing

    def move(self):
            """loops through any number of segments from the LAST segment to the first, moving each to the position of the segment in front of it, thus *following* the first segment"""
            for segnum in range(len(self.segments)-1,0,-1): 
                new_x = self.segments[segnum - 1].xcor()
                new_y = self.segments[segnum - 1].ycor()
                self.segments[segnum].goto(new_x,new_y)
            self.segments[0].forward(MOVE_DISTANCE)
            # self.segments[0].left(90)
