from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # added highscore var
        with open("highscore.txt", mode="r") as file:
            hs = file.read()
            hs_new = int(hs)
        self.high_score = hs_new
        self.color("green")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            hs_new = self.high_score
            with open("highscore.txt", mode="w") as file:
                file.write(str(hs_new))
        self.score = 0
        self.update_scoreboard()
