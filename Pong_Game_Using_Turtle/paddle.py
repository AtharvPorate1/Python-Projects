from turtle import Turtle
PADDLE_COORD = [(350, 0), (350,-20), (350, 20)]
k = 40
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.segments = []
        self.create_paddle(pos)

    def create_paddle(self, pos):


        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos, 0)


        # for i in PADDLE_COORD:
        #     paddleR = Turtle()
        #     paddleR.color("white")
        #     paddleR.penup()
        #     paddleR.shape("square")
        #     paddleR.goto(i)
        #     paddleR.speed("fastest")
        #     paddleR.left(90)

    def up(self):

        newy = k + self.ycor()
        self.goto(self.xcor(), newy)

    def down(self):

        newy = self.ycor() - k
        self.goto(self.xcor(), newy)