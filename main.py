from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect collision with th wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 348:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -348:
        ball.bounce_x()



screen.exitonclick()