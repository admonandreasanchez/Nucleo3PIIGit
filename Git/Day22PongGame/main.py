import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from table import Table
from scoreboard import Scoreboard

#Screen Set up

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game Arcade")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball(10, 10)
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on= True



while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 200:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when the player misses ball, score, reset.

    #righ paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    #left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()







screen.exitonclick()
