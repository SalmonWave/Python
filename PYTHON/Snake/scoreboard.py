from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")

class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0,260)
        self.speed("fastest")
        self.write(arg = f"Score = {self.score}",align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg = f"Score = {self.score}",align = "center", font = FONT)

    def Game_Over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)