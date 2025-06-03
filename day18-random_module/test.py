import turtle as t
import random

# Set up the turtle
t.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

# Set up the screen
screen = t.Screen()
screen.bgcolor("white")

# Function to generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Position the turtle to start drawing
t.goto(-200, 200)

# Create the dot painting
for _ in range(10):  # 10 rows
    for _ in range(10):  # 10 columns
        t.dot(20, random_color())
        t.forward(50)
    t.backward(500)
    t.right(90)
    t.forward(50)
    t.left(90)

# Finish up
screen.exitonclick()