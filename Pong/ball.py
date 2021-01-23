from turtle import Turtle

class Ball(Turtle):
    x_move = 10
    y_move = 10

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(0, 0)
        self.seth(45)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def stroke(self):
        self.x_move *= -1

