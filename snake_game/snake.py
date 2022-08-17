from pickletools import UP_TO_NEWLINE
from turtle import Screen,Turtle
import time

MOVE_DISTANCE = 10
INITIAL_NUM_SEGMENTS = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        # self.add_segment()
    # def add_segment(self):
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
    
    def extend(self):
        target_position = self.segments[-1].position()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(target_position)
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forward(MOVE_DISTANCE)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
            """loops through any number of segments from the LAST segment to the first, moving each to the position of the segment in front of it, thus *following* the first segment"""
            for segnum in range(len(self.segments)-1,0,-1): 
                new_x = self.segments[segnum - 1].xcor()
                new_y = self.segments[segnum - 1].ycor()
                self.segments[segnum].goto(new_x,new_y)
            self.head.forward(MOVE_DISTANCE)
