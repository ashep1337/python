from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # self.high_score =
        self.color("white")
        self.up()
        self.hideturtle()
        self.goto(0, 350)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            (f"Score = {self.score} High Score = {self.high_score}"),
            align="center",
            font=("Arial", 22, "bold"),
        )

    def score_add(self):
        self.score += 1

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()


#        t = Turtle()
#        t.hideturtle()
#        t.color("white")
#        t.write(
#            (f"   Game Over\nYour score is {self.score}"),
#            align="center",
#            font=("Arial", 24, "bold"),
#        )
