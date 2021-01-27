from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PING THAT PONG ALL NIGHT LONG')
screen.tracer(0)

l_paddle = Paddle('left')
r_paddle = Paddle('right')
ball = Ball()
sb = ScoreBoard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.dn, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.dn, "Down")

set_on = True
while set_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect wall collision
    if abs(ball.ycor()) >= 280:
        ball.bounce()

    # detect paddle collison
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.stroke()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.stroke()

    # detect r_paddle miss
    if ball.xcor() >= 380:
        ball.rally_start()
        sb.l_point()
        time.sleep(1)

    # detect l_paddle miss
    if ball.xcor() <= -380:
        ball.rally_start()
        sb.r_point()
        time.sleep(1)

screen.exitonclick()
