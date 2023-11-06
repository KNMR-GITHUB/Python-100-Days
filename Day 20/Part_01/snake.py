from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0




class Snake:

    def __init__(self):
        self.sneks = []
        self.create_snake()
        self.head = self.sneks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snek_body = Turtle("square")
            new_snek_body.penup()
            new_snek_body.color("white")
            new_snek_body.setpos(position)
            self.sneks.append(new_snek_body)

    def move(self):
        for snek_num in range(len(self.sneks) - 1, 0, -1):
            # setting new coordinates for the body parts
            new_x = self.sneks[snek_num - 1].xcor()
            new_y = self.sneks[snek_num - 1].ycor()
            # assigning the new coordinates to the part
            self.sneks[snek_num].setpos(new_x, new_y)
        self.sneks[0].forward(MOVE_DISTANCE)

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
