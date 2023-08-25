from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Dark Red")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # update Scoreboard
    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.clear()
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=-25)
        self.color("orange")
        self.write(f"Your Score is:{self.score}", align=ALIGNMENT, font=("courier", 20, "normal"))
