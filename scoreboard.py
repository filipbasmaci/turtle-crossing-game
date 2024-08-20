from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)

    def show_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.show_level()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over. Your score is: {self.level} ", align="center", font=FONT)
