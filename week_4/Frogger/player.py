from turtle import Turtle


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.up()
        self.shapesize(2, 2)
        self.sety(-380)
        self.seth(90)

    def frog_move(self):
        self.fd(20)


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.pensize(4)
        self.speed("fastest")
        self.teleport(-700, 400)
        self.fd(1400)
        self.teleport(-700, -400)
        self.fd(1400)
