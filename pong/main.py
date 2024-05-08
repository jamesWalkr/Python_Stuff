from turtle import Screen
from paddle import Paddle
from ball import Ball
from  scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    scoreboard.update_scoreboard()

    # Detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left padded misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()


# paddle_1 = Turtle(shape='square')
# paddle_1.shapesize(stretch_wid=5, stretch_len=1)
# paddle_1.color('white')
# paddle_1.penup()
# paddle_1.goto(x=350, y=0)
# def go_up():
#     new_y = paddle_1.ycor() + 20
#     paddle_1.goto(paddle_1.xcor(), new_y)
# def go_down():
#     new_y = paddle_1.ycor() - 20
#     paddle_1.goto(paddle_1.xcor(), new_y)
