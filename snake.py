from turtle import Turtle

STARTING_POSITION = [(-20, 0), (-40, 0), (-60, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):

        for part_num in range(0, 3):
            body_part = Turtle("square")
            body_part.color("white")
            body_part.penup()
            body_part.goto(STARTING_POSITION[part_num])
            self.segments.append(body_part)

    def move(self):

        for part_num in range(len(self.segments) - 1, 0, -1):
            new_loc = (self.segments[part_num - 1].xcor(), self.segments[part_num - 1].ycor())
            self.segments[part_num].goto(new_loc)

        self.snake_head.forward(20)

    def grow(self):
        app_loc = self.segments[-1].xcor(), self.segments[-1].ycor()
        body_part = Turtle("square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(app_loc)
        self.segments.append(body_part)

    def up(self):
        if self.snake_head.heading() in [90, 270]:
            return
        else:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() in [270, 90]:
            return
        else:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() in [180, 0]:
            return
        else:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() in [0, 180]:
            return
        else:
            self.snake_head.setheading(0)
