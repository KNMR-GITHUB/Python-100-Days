from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()

# higher order functionalities
# sending a function as an input for another function

screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
