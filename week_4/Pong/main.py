import time
from turtle import Screen

from ball import Ball
from paddles import Border, Paddle
from score import Scoreboard

screen = Screen()
screen.colormode(255)
screen.bgcolor(0, 0, 0)
screen.listen()
screen.tracer(0)

r_paddle = Paddle(620, 300)
l_paddle = Paddle(-620, 300)
screen = Screen()
ball = Ball()
border = Border()
score = Scoreboard()

screen.onkey(l_paddle.paddle_up, key="Up")
screen.onkey(l_paddle.paddle_down, key="Down")
screen.onkey(r_paddle.paddle_up, key="w")
screen.onkey(r_paddle.paddle_down, key="s")

game = True


while game:
    screen.update()
    ball.move()
    time.sleep(0.01)
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -600:
        ball.bounce_x()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 600:
        ball.bounce_x()

    if ball.xcor() > 650:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -650:
        ball.reset_position()
        score.r_point()
