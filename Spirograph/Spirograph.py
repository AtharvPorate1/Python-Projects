import turtle
from turtle import Turtle,Screen,colormode
import random
turtle.colormode(255)
raju = Turtle()
screen = Screen()
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
size = 5
for spirograph in range(0,int(360/size)):
    raju.speed("fastest")
    size = 5
    raju.pencolor(random_color())
    raju.circle(100)
    current_heading = raju.heading()
    raju.setheading(current_heading + size)
screen.exitonclick()
