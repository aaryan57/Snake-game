from turtle import Turtle
STARTING_POSITIONS=([0,0],[-20,0],[-40,0])
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class snake:
    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0]
    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.add(position)
    def add(self,position):
        segment_2 = Turtle("square")
        segment_2.color("white")
        segment_2.penup()
        segment_2.goto(position)
        self.segments.append(segment_2)
    def extend(self):
        self.add(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def reset_snake(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]
