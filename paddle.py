from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, player_location):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('white')
        self.location(player_location)

    def location(self, player_location):
        self.setx(player_location)

    def move_up(self):
        self.forward(60)

    def move_down(self):
        self.back(60)

