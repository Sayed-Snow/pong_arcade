from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 22, 'normal'))

    def placement(self, x_value):
        self.goto(y=340, x=x_value)
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 22, 'normal'))


