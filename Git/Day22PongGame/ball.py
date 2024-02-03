from turtle import Turtle
import time

dx = 10  # Cambio en la posición en el eje x
dy = -10  # Cambio en la posición en el eje y

class Ball(Turtle):


    def __init__(self, dx, dy):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.speed('fastest')
        self.color('white')
        self.x_move = dx  # Asignar dx al atributo dx de la instancia
        self.y_move = dy  # Asignar dy al atributo dy de la instancia
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()












