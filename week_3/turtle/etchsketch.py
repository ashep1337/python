from turtle import Screen, Turtle

t = Turtle()
screen = Screen()


def move_fd():
    t.fd(10)


def move_bk():
    t.bk(10)


def move_lt():
    t.lt(10)


def move_rt():
    t.rt(10)


def clear():
    t.reset()


screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="a", fun=move_lt)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="d", fun=move_rt)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
