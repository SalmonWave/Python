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
        with open("HIGH_SCORE.txt","r") as HIGH_SCORE:
            self.highscore = int(HIGH_SCORE.read())
        self.goto(0,260)
        self.speed("fastest")
        self.write(arg = f"Score = {self.score}      HIGH SCORE : {self.highscore}",align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(arg = f"SCORE : {self.score}      HIGH SCORE : {self.highscore}",align = "center", font = FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("HIGH_SCORE.txt","w") as HIGH_SCORE:
                HIGH_SCORE.write(str(self.highscore))

        self.score = 0
        self.update_scoreboard()
    # def Game_Over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)