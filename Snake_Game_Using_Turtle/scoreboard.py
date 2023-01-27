from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
file = open("high_score.txt", mode="r")
content = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.high_score = int(content)
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)