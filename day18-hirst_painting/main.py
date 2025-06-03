import turtle
from turtle import Turtle, Screen
import random

colors = [(234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15),
          (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168),
          (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163),
          (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34),
          (131, 217, 230), (183, 17, 9), (12, 96, 52), (166, 182, 235), (242, 167, 153), (10, 85, 102),
          (252, 5, 48), (66, 94, 8), (248, 13, 10), (14, 48, 249)]

t = Turtle()
turtle.colormode(255)
t.pensize(20)
x = -250 #coordinates for the turtle to go to
y = -250

for _ in range(10):
    t.penup()
    t.goto(x, y)
    for _ in range(10):
        t.dot(20, (random.choice(colors)))
        t.penup()
        t.fd(50)
    y += 50
t.hideturtle()

screen = Screen()
screen.exitonclick()