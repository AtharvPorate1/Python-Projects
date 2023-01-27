from turtle import Turtle
from player import STARTING_POSITION
FONT = ("Courier", 10, "normal")
ALIGNMENT = "Center"
LEVEL = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 270)
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level : {self.level}", False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(STARTING_POSITION)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)


