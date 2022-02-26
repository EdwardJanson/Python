from turtle import Turtle
FORWARD = 40


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.setposition(position)

    def up(self):
        new_y = self.ycor() + FORWARD
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - FORWARD
        self.goto(self.xcor(), new_y)
