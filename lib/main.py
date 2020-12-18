from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
import time

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1500

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.title("PyPong")

right_paddle = Paddle((SCREEN_WIDTH * 0.5 - 50, 0))
left_paddle = Paddle((SCREEN_WIDTH * -0.5 + 50, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > (SCREEN_HEIGHT - 520) or ball.ycor() < (SCREEN_HEIGHT * -1 + 520):
        ball.bounce()




screen.exitonclick()