from turtle import Screen
from paddle import Paddle
from Ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)


screen.listen()
screen.onkey(l_paddle.move_up, "W")
screen.onkey(l_paddle.move_down, "S")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.initialize_position()
        scoreboard.left_score()


    if ball.xcor() < -380:
        ball.initialize_position()
        scoreboard.right_score()