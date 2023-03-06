from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.setheading(45)

    def move(self):
        self.forward(20)

    def top_bottom_bounce(self):
        direction = self.heading()
        if 90 < direction < 180 or 270 < direction < 360:
            self.setheading(90 + direction)
        else:
            self.setheading(270 + direction)

    def player_bounce(self):
        direction = self.heading()
        if 0 < direction < 90 or 180 < direction < 270:
            self.setheading(90 + direction)
        else:
            self.setheading(270 + direction)

        speed = self.speed() + 1
        self.speed(speed)

    def restart(self):
        self.player_bounce()
        self.goto(0, 0)
