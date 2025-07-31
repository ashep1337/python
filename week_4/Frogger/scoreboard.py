from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.teleport(-500, 350)
        self.up()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.teleport(-500, 330)
        self.write(
            (f"Level: {self.score}"), align="center", font=("Courier", 40, "normal")
        )
        self.score += 1

    def game_over(self):
        self.teleport(0, 0)
        self.write("Game Over", align="center", font=("Arial", 36, "bold"))
