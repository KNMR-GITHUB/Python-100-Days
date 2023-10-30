from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
tim = timmy_the_turtle

tim.shape("turtle")
tim.color("navyBlue")


for i in range(0, 4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()
