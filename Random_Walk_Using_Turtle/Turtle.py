import turtle
from turtle import Turtle,Screen,colormode
import random
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


raju = Turtle()

for walk in range(0,200):

    x = random.randint(0, 3)
    raju.pencolor(random_color())
    raju.width(10)
    raju.speed(6)
    raju.fd(30*x)
    raju.right(90*x)








screen = Screen()
screen.exitonclick()
