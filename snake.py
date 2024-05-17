import turtle as t 
import time

MOVE_SNAKE = 20
UP = 90
DOWN = 270 
LEFT = 180
RIGHT = 0 
POSITION_LIST = [(0, 0), (-20, 0), (-40, 0)]  

class Snake:
    def __init__(self): 
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITION_LIST:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = t.Turtle("square")
        time.sleep(0.1)
        new_segment.speed("fastest")
        new_segment.hideturtle()
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        new_segment.showturtle()
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def move(self):
        for new_segment in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[new_segment - 1].xcor()
            y_pos = self.segments[new_segment - 1].ycor()
            self.segments[new_segment].goto(x_pos, y_pos)
        self.head.hideturtle()
        # self.head.left(90)
        self.head.showturtle()
        self.head.forward(MOVE_SNAKE)
        
 

"""
Tricks for making Classes:
1.All things should enter in def or functions
2.Most of the things must start with self
3.for loops should exist in functions not outside singly.
4.All variables should start with self.name_of_variables
"""
