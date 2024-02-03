import turtle
from turtle import Turtle


WALL_POSITIONS = [(-400, 300), (-400, -300)]
DISTANCE= 10

class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.top_wall = []
        self.bottom_wall = []

    def create_wall(self):
        for position in WALL_POSITIONS:
            self.create_walls()

    def create_walls(self):
        top_wall = Turtle(shape="square")
        top_wall.color('white')
        top_wall.penup()
        top_wall.goto(-400, 300)
        top_wall.shapesize(0.5, 80)
        top_wall.pendown()

        bottom_wall = Turtle(shape="square")
        bottom_wall.color('white')
        bottom_wall.penup()
        bottom_wall.goto(-400, -300)
        bottom_wall.shapesize(0.5, 80)
        bottom_wall.pendown()







