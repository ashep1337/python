import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(1, 1)
        self.up()
        self.refresh()

    def refresh(self):
        randx = random.randrange(-560, 560, 20)
        randy = random.randrange(-320, 320, 20)
        self.goto(randx, randy)
