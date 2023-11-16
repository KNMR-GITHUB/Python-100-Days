from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_collision(self):
        self.y_move *= -1
        self.speedup()

    def paddle_collision(self):
        self.x_move *= -1
        self.speedup()

    def restart(self, turn):
        self.goto(0, 0)

        if turn == "p1":
            self.x_move = -10
            self.y_move = -10
        elif turn == "p2":
            self.x_move = 10
            self.y_move = 10

        self.x_move *= -1
        self.y_move *= -1

    def speedup(self):
        self.x_move = self.x_move * 1.13
        self.y_move = self.y_move * 1.13
