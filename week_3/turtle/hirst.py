# import colorgram
#
# colors = colorgram.extract("hirst.jpg", 30)
#
# pick_color = colors[random.randint(0, 29)]
#
# print(pick_color.rgb)
#
#
# rgb_colors = []
#
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    rgb_colors.append(, b)
#
# print(rgb_colors)

import random
import turtle

from colors import color_choices

screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor(0, 0, 0)

t = turtle.Turtle()
t.hideturtle()
t.up()
x = -250
y = -250


def set_coords():
    t.setx(x)
    t.sety(y)


def move_up():
    global x
    global y
    y += 50
    set_coords()


def print_row():
    for n in range(10):
        dot_color = color_choices[random.randint(0, 27)]
        t.dot(20, dot_color)
        t.forward(60)


for n in range(10):
    set_coords()
    print_row()
    move_up()


screen.exitonclick()
