from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
import time

screen = Screen()
screen.setup(width=1500, height=1000)
screen.bgcolor("black")
screen.tracer(0)
screen.title("PyPong")

right_paddle = Paddle((700, 0))
left_paddle = Paddle((-700, 0))
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






screen.exitonclick()