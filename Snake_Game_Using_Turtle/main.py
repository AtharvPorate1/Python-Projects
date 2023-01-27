import time
from turtle import *
from Snake import *
from food import *
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

food.refresh()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:

    screen.update()
    time.sleep(.1)
    snake.move()

    # collision detection
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.reset()
        snake.reset()

    #collision with tail

    for segment in snake.snake[1:]:

        if snake.head.distance(segment) < 10:

            scoreboard.reset()
            snake.reset()















screen.exitonclick()