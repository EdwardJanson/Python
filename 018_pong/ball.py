from turtle import Turtle
import time
START_HEADING = 50
FORWARD = 10
SPEED = 0.05


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(START_HEADING)
        self.ball_speed = SPEED

    def new_y_heading(self):
        self.setheading(360 - self.heading())
        self.forward(FORWARD)

    def new_x_heading(self):
        if self.heading() >= 180:
            self.setheading((360 - self.heading()) + 180)
        else:
            self.setheading(360 - (self.heading() - 180))
        self.forward(FORWARD)

    def move(self, r_paddle, l_paddle):
        time.sleep(self.ball_speed)
        if self.ycor() > 280 or self.ycor() < -280:
            self.new_y_heading()
        if self.xcor() > 330 and self.distance(r_paddle) < 50 or self.xcor() < -330 and self.distance(l_paddle) < 50:
            self.new_x_heading()
            if self.ball_speed > 0.01:
                self.ball_speed *= 0.9
        elif self.xcor() > 380 or self.xcor() < -380:
            if self.xcor() > 380:
                self.reset_position()
                self.ball_speed = SPEED
                return "r_loss"
            else:
                self.reset_position()
                self.ball_speed = SPEED
                return "l_loss"
        else:
            self.forward(FORWARD)

    def reset_position(self):
        self.setposition(0, 0)
        self.new_x_heading()
