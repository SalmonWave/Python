from turtle import Turtle

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH,0)
        self.penup()
        self.speed(0)
        self.goto(position)

    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
