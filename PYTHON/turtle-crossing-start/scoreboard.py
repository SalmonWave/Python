FONT = ("Courier", 24, "normal")
import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1

    def update_level(self):
        self.clear()
        self.write(arg = f"LEVEL : {self.level}", font = FONT, align = "left")


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg = "GAME OVER", font = FONT, align = "center")

    def level_up(self):
        self.level += 1
