import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)
        self.direction = 1
        self.speed = 10
        self.min_y = -300
        self.max_y = 300

    def paddle_up(self):
        if self.ycor() < 300:
            self.sety(self.ycor() + 20)

    def paddle_down(self):
        if self.ycor() > -300:
            self.sety(self.ycor() - 20)

    def computer_move(self):
        y = self.ycor()
        y += self.direction * self.speed
        self.sety(y)

        if y >= self.max_y:
            self.direction = -1
        elif y <= self.min_y:
            self.direction = 1

        turtle.getscreen().ontimer(self.computer_move, 40)


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.pensize(4)
        self.goto(-640, 350)
        self.down()
        self.fd(1280)
        self.penup()
        self.goto(-640, -350)
        self.pendown()
        self.fd(1280)
