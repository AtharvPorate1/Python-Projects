from turtle import Turtle, Screen, colormode

raju = Turtle()
screen = Screen()


def forward():
    raju.forward(10)


def backward():
    raju.backward(10)


def right():
    raju.right(7.5)


def left():
    raju.left(7.5)


def freemove():
    if not raju.isdown():
        raju.pendown()
    else:
        raju.penup()


def resetscreen():

    raju.clear()
    raju.penup()
    raju.home()
    raju.pendown()




screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="a", fun=left)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=right)
screen.onkey(key="space", fun=freemove)
screen.onkey(key="c", fun=resetscreen)


screen.exitonclick()