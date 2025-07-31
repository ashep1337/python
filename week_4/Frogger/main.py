from turtle import Screen

from car_manager import Car
from player import Border, Frog
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.listen()

frog = Frog()
border = Border()
scoreboard = Scoreboard()
car = Car()


frog.frog_move()
screen.onkeyrelease(frog.frog_move, "w")

game = True
while game:
    screen.update()
    car.create_car()
    car.move()

    for _ in car.all_cars:
        if frog.distance(_) < 30:
            game = False
            scoreboard.game_over()
    if frog.ycor() >= 400:
        frog.teleport(0, -380)
        car.speed_up()
        scoreboard.update_score()

screen.exitonclick()
