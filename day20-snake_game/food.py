from turtle import Turtle
import random

class Food(Turtle): #Inheriting from the turtle superclass

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #This changes the size of the circle to half (default is
        # 20 by 20 pixel. In this case, it is 10/10 pixel
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
