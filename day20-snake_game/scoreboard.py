from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.update()
