from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        """Increase score each time the turtle successfully crosses"""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        """Write game over on the screen"""
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
