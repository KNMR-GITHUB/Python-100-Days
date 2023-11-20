import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("India States Game")

image = "Imap.gif"
screen.addshape(image)
turtle.shape(image)

# read csv
states_data = pd.read_csv("29_states.csv")
# list to check
names = states_data["state"].to_list()
x_coordinates = states_data["x"].to_list()
y_coordinates = states_data["y"].to_list()

# setting up a pen
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color("green")

# To get coordinates of mouse click on turtle screen.
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)

# first prompt
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

# game loop

score = 0
guessed_states = []
lives = 3

while len(guessed_states) < 29:

    # if player does not know any more states
    if answer_state == "Exit":
        # missed states
        missing_states = []
        for state in names:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)

        # converting to df
        new_df = pd.DataFrame(missing_states)
        new_df.to_csv("States_to_learn.csv")
        break

    for i in range(0, len(names)):
        if answer_state == names[i]:
            x_cor = int(x_coordinates[i])
            y_cor = int(y_coordinates[i])

            # writing on the screen
            pen.goto(x_cor, y_cor)
            pen.write(names[i])

            guessed_states.append(names[i])
            score += 1
        else:
            lives -= 1

    answer_state = screen.textinput(title=f"{score}/29 States Correct", prompt="What's another state's name?").title()
