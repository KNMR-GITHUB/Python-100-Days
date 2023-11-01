from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

is_race_on = False

user_choice = screen.textinput(title="Pick your turtle", prompt="Which turtle will win the race? Enter a color: ")
color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_list = []
y_axis = -100

for i in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.color(color_list[i])
    tim.penup()
    tim.setpos(x=-230, y=y_axis)
    y_axis += 30
    turtle_list.append(tim)

if user_choice:
    is_race_on = True

while is_race_on:
    for i in range(0, 7):
        if turtle_list[i].xcor() > 230:
            is_race_on = False
            winner = turtle_list[i].pencolor()
            if user_choice == winner:
                print(f"You won ! The winner was turtle {winner}")
            else:
                print(f"You lost ! The winner was turtle {winner}")
            break

        pace = random.randint(1, 10)
        turtle_list[i].forward(pace)

screen.exitonclick()
