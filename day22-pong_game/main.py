from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Create a pedal
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#Create the ball
ball = Ball()
scoreboard = Scoreboard()


#Control the left and right paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect if the right paddle misses the ball
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.left_score_increment()

    #Detect if the left paddle misses the ball
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.right_score_increment()

    #Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    print(ball.move_speed)








screen.exitonclick()