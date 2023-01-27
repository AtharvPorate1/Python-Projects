from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting Up Screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)
screen.listen()

# Game Object Creation
paddleR = Paddle(350)
paddleL = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()





# Game Loop

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    screen.onkey(paddleR.up, "Up")
    screen.onkey(paddleR.down, "Down")
    screen.onkey(paddleL.up, "w")
    screen.onkey(paddleL.down, "s")
    ball.move()

    # Collision Detection with walls

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    # Collision with paddle

    if ball.distance(paddleR) < 50 and ball.xcor() > 320 or ball.distance(paddleL) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # If ball goes out of bounds

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_scored()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_scored()






screen.exitonclick()