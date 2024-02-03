from turtle import Turtle

MOVEMENT_SPEED = 20

STARTING_POSITION = [(-350, 0), (350, 0)]

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.screen.update()

    def up(self):
        if self.ycor() < 300:
            self.goto(self.xcor(), self.ycor() + MOVEMENT_SPEED)
            print((self.ycor()))
        else:
            pass

    def down(self):
        if self.ycor() > -300:
            self.goto(self.xcor(), self.ycor()-MOVEMENT_SPEED)
        else:
            pass






