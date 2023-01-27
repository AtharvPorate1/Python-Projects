from turtle import Turtle

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]




class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.color(COLORS[random.randint(0, 5)])
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

        self.goto(random.randint(-250, 500), random.randint(-250, 250))
        self.move()

    def move(self):
        self.setheading(180)
        if self.xcor() < -350:
            self.goto(400, self.ycor())
        elif self.xcor() > -360:
            self.fd(self.STARTING_MOVE_DISTANCE)


    def difficulty(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT







