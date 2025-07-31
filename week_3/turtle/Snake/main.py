import time
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.colormode(255)
screen.bgcolor(0, 0, 0)
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

snake.create_border()

game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.border()
    if snake.border() is False:
        score.game_over()
        snake.reset()
        # game = False
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.add_segment()
        score.score_add()
        score.update_score()
    for n in snake.segments[1:]:
        if snake.head.distance(n) < 10:
            # game = False
            score.game_over()
            snake.reset()
screen.exitonclick()
