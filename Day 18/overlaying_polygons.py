from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
tim = timmy_the_turtle

tim.shape("turtle")

color_list = ["red", "blue", "green", "yellow", "orange", "pink", "violet", "black"]

for i in range(3, 11):
    angle = 360/i
    tim.color(color_list[i - 3])
    for j in range(0, i):

        tim.right(angle)
        tim.forward(80)


screen = Screen()
screen.exitonclick()

