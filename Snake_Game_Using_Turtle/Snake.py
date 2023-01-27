
from turtle import *


class Snake:

    def __init__(self):

        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake = []
        self.create_snake()

    def create_snake(self):

        for position in self.starting_positions:
            self.add_segment(position)
        self.head = self.snake[0]
        self.head.color("red")

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        new_segment.shape("square")

        self.snake.append(new_segment)



    def extend(self):
        self.add_segment(self.snake[-1].position())


    def move(self):

        for i in range(len(self.snake) - 1, 0, -1):
            xcord = self.snake[i - 1].xcor()
            ycord = self.snake[i - 1].ycor()

            self.snake[i].goto(xcord, ycord)
        self.snake[0].fd(20)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
