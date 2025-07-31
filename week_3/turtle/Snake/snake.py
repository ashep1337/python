from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        for _ in range(3):
            self.add_segment()
        self.head = self.segments[0]

    def add_segment(self):
        segment = Turtle("square")
        segment.up()
        segment.color("white")
        if self.segments:
            last_segment = self.segments[-1]
            segment.goto(last_segment.pos())
        else:
            segment.goto(0, 0)
        self.segments.append(segment)

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[n - 1].xcor()
            y_cor = self.segments[n - 1].ycor()
            self.segments[n].goto(x_cor, y_cor)
        self.segments[0].fd(20)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.__init__()
        self.head = self.segments[0]

    def border(self):
        if (
            self.segments[0].xcor() > 600
            or self.segments[0].xcor() < -600
            or self.segments[0].ycor() > 340
            or self.segments[0].ycor() < -340
        ):
            return False

    def create_border(self):
        border = Turtle()
        border.hideturtle()
        border.pensize(4)
        border.color("white")  # Border color
        border.penup()
        border.goto(-600, 340)
        border.pendown()

        for _ in range(2):
            border.forward(1200)
            border.right(90)
            border.forward(680)
            border.right(90)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)
