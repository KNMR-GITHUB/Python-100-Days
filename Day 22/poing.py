from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p2.go_up, "w")
screen.onkey(p2.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_collision()
    # paddle collision
    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.paddle_collision()
    # out of bounds
    if ball.xcor() > 380:
        p2_turn = "p2"
        ball.restart(p2_turn)
        scoreboard.score_increase_p2()
    elif ball.xcor() < -380:
        p1_turn = "p1"
        ball.restart(p1_turn)
        scoreboard.score_increase_p1()

screen.exitonclick()
