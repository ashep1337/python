import random
import turtle

screen = turtle.Screen()
screen.colormode(255)

t = turtle.Turtle()
t.speed(10)
t.pensize(10)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


n = [0, 90, 180, 270]

screen.bgcolor(0, 0, 0)
while True:
    t.color(random_color())
    angle = random.choice(n)
    t.setheading(angle)
    t.forward(20)
