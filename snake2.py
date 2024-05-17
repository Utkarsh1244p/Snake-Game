import turtle as t 

MOVE_SNAKE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40,0)]

class Snake:
    def __init__(self): 
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = t.Turtle("square")
            new_segment.speed(0)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            x_pos = self.segment[seg_num - 1].xcor()
            y_pos = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x_pos, y_pos)
        self.segment[0].hideturtle()
        # self.turtle_list[0].left(90)
        self.segment[0].showturtle()
        self.segment[0].forward(MOVE_SNAKE)
        


"""
Tricks for making Classes:
1.All things should enter in def or functions
2.Most of the things must start with self
3.for loops should exist in functions not outside singly.
4.All variables should start with self.name_of_variables
"""
