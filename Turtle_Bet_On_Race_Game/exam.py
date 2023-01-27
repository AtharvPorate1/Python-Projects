#Race
import random
from turtle import *

screen = Screen()
screen.setup(width=500, height=400)

color = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
players = []
userBet = screen.textinput(title("Make a bet"), prompt="Input the color you wanna bet on :")
isRacing = False
print(userBet)

for qwe in range(0, 7):
    newTurtle = Turtle()
    newTurtle.shape("turtle")
    newTurtle.color(color[qwe])
    newTurtle.penup()
    newTurtle.goto(-230, qwe * 30 - 70)
    players.append(newTurtle)

if userBet:
    isRacing = True

while isRacing:

    for player in players:
        if player.xcor() > 230:
            isRacing = False
            winnerColor = player.pencolor()
            if userBet == winnerColor:
                print(f"You have won, {winnerColor} is the winner")
            else:
                print(f"You have lost, {winnerColor} is the winner")
        randDist = random.randint(0, 20)
        player.fd(randDist)








# raju.color("red")
# raju.penup()
# raju.goto(-240,-100)
#birju.color("blue")
#sarju.color("pink")
#farju.color("green")

























screen.exitonclick()
