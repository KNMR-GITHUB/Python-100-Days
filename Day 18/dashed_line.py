from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
tim = timmy_the_turtle

tim.shape("turtle")


for i in range(0, 50):

    tim.color("navyBlue")
    tim.forward(5)
    tim.color("white")
    tim.forward(2)

screen = Screen()
screen.exitonclick()
