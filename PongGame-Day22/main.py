from turtle import Screen
import time
from scoreboard import ScoreBoard
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0))
scoreboard = ScoreBoard()
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# detect the ball collision with wall and then change the direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.xcor() > 360 and ball.distance(r_paddle) < 20 or ball.xcor() < -360 and ball.distance(l_paddle) < 20:
        ball.bounce_x()

    #detect r_paddle misses
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.increase_score_l()

    # detect l_paddle misses
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.increase_score_r()

screen.exitonclick()