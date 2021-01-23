from turtle import Screen
import time
from paddle import Paddle
from ball import Ball


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PING THAT PONG ALL NIGHT LONG')
screen.tracer(0)

l_paddle = Paddle('left')
r_paddle = Paddle('right')
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.dn, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.dn, "Down")

set_on = True
while set_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #detect wall collision
    if abs(ball.ycor()) >= 280:
        ball.bounce()
    #detect paddle collison
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.stroke()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.stroke()
    #if abs(ball.xcor()) >=400:
    #    point!

screen.exitonclick()
