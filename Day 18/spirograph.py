import turtle
import random

# creating object
tim = turtle.Turtle()

# changing color mode to 255 to support rgb format
turtle.colormode(255)

# defining the shape
tim.shape("turtle")

# possible angles
walk_angle = [0, 90, 180, 270]

# random color function


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_radius():
    rad = random.randint(40, 100)
    return rad


# speed of the turtle
tim.speed(0)

# main loop
for i in range(0, 100):
    # r_color = random_color()
    tim.color("lightBlue")
    # radius = random_radius()
    tim.circle(100)
    tim.color("skyBlue")
    tim.circle(80)
    tim.color("blue")
    tim.circle(60)
    tim.color("navyBlue")
    tim.circle(40)
    tim.color("darkBlue")
    tim.circle(20)
    tim.left(5)


screen = turtle.Screen()
screen.exitonclick()
