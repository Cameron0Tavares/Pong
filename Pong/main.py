from turtle import Screen
import time
from paddle import Paddle


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PING THAT PONG ALL NIGHT LONG')
screen.tracer(0)

left = Paddle('left')
right = Paddle('right')


screen.listen()
screen.onkey(left.up, "w")
screen.onkey(left.dn, "s")
screen.onkey(right.up, "Up")
screen.onkey(right.dn, "Down")

rally_on = True
while rally_on:
    screen.update()
    time.sleep(0.1)



screen.exitonclick()
