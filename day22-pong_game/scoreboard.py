from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the score everytime a player misses the ball"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def right_score_increment(self):
        """Increase right score"""
        self.goto(100, 200)
        self.r_score += 1
        self.update_scoreboard()

    def left_score_increment(self):
        """Increase left score"""
        self.goto(-100, 200)
        self.l_score += 1
        self.update_scoreboard()