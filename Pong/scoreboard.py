from turtle import Turtle


class ScoreBoard(Turtle):
    l_score = 0
    r_score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 60, 'bold'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 60, 'bold'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
