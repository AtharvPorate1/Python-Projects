from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)


    def refresh(self):
        xcord = random.randint(-280, 280)
        ycord = random.randint(-280, 280)
        self.goto(xcord, ycord)


