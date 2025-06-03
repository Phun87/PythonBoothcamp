from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# Screen setting
screen = Screen()
snake = Snake()
food = Food()
score = Score()

screen.title("Snake Game")
screen.bgcolor("light sky blue")
screen.setup(width=600, height=600)
screen.tracer(0) #Use this method to turn off the turtle animation

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #Detect collision with food using distance method from turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()