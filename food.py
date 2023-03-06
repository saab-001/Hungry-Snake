import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.shape("circle")
        self.shapesize(0.6, 0.6)
        self.create_food()

    def create_food(self):
        rand_loc = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(rand_loc)

    def reappear(self):
        rand_loc = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(rand_loc)
