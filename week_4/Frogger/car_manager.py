import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SPEED = 0.05
CAR_CHANCE = 1000


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.1
        self.chance = 500

    def create_car(self):
        if random.randint(1, self.chance) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 3)
            new_car.color(random.choice(COLORS))
            new_car.up()
            new_car.teleport(750, random.randint(-340, 400))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.bk(self.car_speed)
            if car.xcor() < -800:
                car.hideturtle()
                self.all_cars.remove(car)
                del car

    def speed_up(self):
        self.car_speed += 0.02
        self.chance = max(1, self.chance - 50)
        print(self.car_speed)
        print(self.chance)
        print(len(self.all_cars))
