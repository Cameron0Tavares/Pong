from turtle import Turtle
LEFT_POS = (-350, 0)
RIGHT_POS = (350, 0)


class Paddle(Turtle):

    def __init__(self, screen_side):
        super().__init__()
        self.penup()
        self.color('white')
        self.create_paddle()
        if screen_side == 'right':
            self.goto(RIGHT_POS)
        else:
            self.goto(LEFT_POS)

    def create_paddle(self):
        self.shape('square')
        self.shapesize(stretch_len=5)
        self.seth(90)

    def up(self):
        self.forward(20)

    def dn(self):
        self.backward(20)
