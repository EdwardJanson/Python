from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_part(position)

    def add_snake_part(self, position):
        snake_part = Turtle("square")
        snake_part.penup()
        snake_part.color("white")
        snake_part.goto(position)
        self.snake.append(snake_part)

    def extend_snake(self):
        self.add_snake_part(self.snake[-1].position())

    def move(self):
        for part_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part_num - 1].xcor()
            new_y = self.snake[part_num - 1].ycor()
            self.snake[part_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
