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


# width of the lines
tim.width(8)

# speed of the turtle
tim.speed(0)

# main loop
for i in range(0, 200):
    r_walk_angle = walk_angle[random.randint(0, 3)]
    r_walk_angle_2 = walk_angle[random.randint(0, 3)]
    r_color = random_color()
    r_color_2 = random_color()
    tim.color(r_color)
    tim.forward(30)
    tim.left(r_walk_angle)
    tim.color(r_color_2)
    tim.forward(30)
    tim.right(r_walk_angle_2)

screen = turtle.Screen()
screen.exitonclick()
