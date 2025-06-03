from turtle import Turtle, Screen
import random
a = 230
for _ in range(2): #This creates a finish line (2 white lines)
    tim = Turtle()
    tim.penup()
    tim.goto(a, 210)
    tim.color("white")
    tim.pensize(10)
    tim.pendown()
    tim.goto(a, -210)
    a -= 11

screen = Screen()
screen.setup(width=500, height=400)
screen.bgpic("background.gif") # Sets the background
screen.title("Welcome to Turtle Race") #Title of the window
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour in Rainbow colors: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red", ]
all_turtles = []
x = -230
y = -150
is_race_on = False
for color in colors:
    t = Turtle()
    t.penup()
    t.shape("turtle")
    t.color(color)
    t.goto(x, y)
    y += 50
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have Won! The {winning_color} is the winner.")
                pen = Turtle() # This is for the final text display
                pen.color("blue")
                pen.hideturtle()
                pen.penup()
                pen.goto(-100, 0)
                pen.write("You have Won!", font=('Arial', 24, 'normal'))
            else:
                print(f"You have Lost! The {winning_color} is the winner.")
                pen = Turtle() #This is for the final text display
                pen.color("blue")
                pen.hideturtle()
                pen.penup()
                pen.goto(-100, 0)
                pen.write("You have Lost!", font=('Arial', 24, 'normal'))
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()