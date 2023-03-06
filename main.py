from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

speed = 0.09
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.screensize(canvwidth=800, canvheight=600)
screen.title('Pong')

right_player = Paddle(350)
left_player = Paddle(-350)
ball = Ball()
l_score = Scoreboard()
r_score = Scoreboard()
r_score.placement(-120)
l_score.placement(120)
screen.listen()
screen.onkey(key='Up', fun=right_player.move_up)
screen.onkey(key='Down', fun=right_player.move_down)
screen.onkey(key='w', fun=left_player.move_up)
screen.onkey(key='s', fun=left_player.move_down)

while not r_score.score == 5 or l_score.score == 5:
    time.sleep(speed)
    ball.move()
    if ball.ycor() > 390 or ball.ycor() < -390:
        ball.top_bottom_bounce()

    if ball.distance(right_player) < 40 or ball.distance(left_player) < 40:
        ball.player_bounce()

        if speed > 0.01:
            speed = speed - 0.01

    if ball.xcor() > 500:
        ball.restart()
        speed = 0.08
        r_score.increase()

    if ball.xcor() < -500:
        ball.restart()
        speed = 0.08
        l_score.increase()

    screen.update()

screen.exitonclick()
