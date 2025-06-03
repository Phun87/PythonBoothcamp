import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255) # This sets the colormode to rgb. Notice here we tap into the
# turtle module rather than the t object
angle = 5
def gen_colour_num():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r, g, b)
    return colour_tuple














screen = Screen()
screen.exitonclick()