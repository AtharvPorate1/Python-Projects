import random
import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard


# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Game Object
cars = []
player = Player()
scoreboard = Scoreboard()

for i in range(0, 25):
    car = CarManager()
    cars.append(car)

print(player.xcor())
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Player Movement
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")
    screen.onkey(player.move_left, "Left")
    screen.onkey(player.move_right, "Right")

    # Car Manager

    for i in cars:
        i.move()

    # Collision with cars

    for i in cars:
        if i.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Increase Level

    if player.ycor() > 280:

        scoreboard.increase_level()
        player.goto(STARTING_POSITION)
        for i in cars:
            i.difficulty()







screen.exitonclick()




