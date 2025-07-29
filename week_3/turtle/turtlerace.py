import random
from turtle import Screen, Turtle

screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="What color will win?")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-70, -40, -10, 20, 50, 80]
screen.setup(500, 400)
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.up()
    new_turtle.goto(x=-230, y=y_axis[turtle_index])
    all_turtles.append(new_turtle)

game = True

while game:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            game = False
            winner = turtle.pencolor()

            if winner == user_bet.lower():
                print(f"The winner is {winner}. You Win!")
            else:
                print(f"The winner is {winner}. You lose!")

        move = random.randint(1, 10)
        turtle.fd(move)

screen.exitonclick()
