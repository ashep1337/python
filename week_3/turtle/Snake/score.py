from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.up()
        self.hideturtle()
        self.goto(0, 350)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            (f"Score = {self.score}"), align="center", font=("Arial", 22, "bold")
        )

    def score_add(self):
        self.score += 1

    def game_over(self):
        t = Turtle()
        t.hideturtle()
        t.color("white")
        t.write(
            (f"   Game Over\nYour score is {self.score}"),
            align="center",
            font=("Arial", 24, "bold"),
        )
