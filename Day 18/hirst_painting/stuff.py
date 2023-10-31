import colorgram
import turtle
import random

# creating object
tim = turtle.Turtle()

# changing color mode to 255 to support rgb format
turtle.colormode(255)

tim.speed(0)

# defining the shape
tim.shape("turtle")

colors = colorgram.extract('hirst.jpg', 10)
color_list = []
for i in colors:
    color_tuple = (i.rgb.r, i.rgb.g, i.rgb.b)
    color_list.append(color_tuple)

print(color_list)

y_axis = -180.0

tim.penup()

tim.setpos(-180.0, -1800.0)

for i in range(0, 10):
    for j in range(0, 10):
        tim.pendown()
        current_color = color_list[random.randint(0, 9)]
        tim.dot(16, current_color)
        tim.penup()
        tim.forward(40)
    y_axis += 40.0
    tim.setpos(-180.0, y_axis)

screen = turtle.Screen()
screen.exitonclick()
