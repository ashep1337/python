import random
import turtle

screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor(0, 0, 0)

t = turtle.Turtle()
t.speed("fastest")
t.pensize(5)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


gap = 5

for n in range(int(360 / gap)):
    t.color(random_color())
    t.circle(200)
    t.left(gap)

screen.exitonclick()
