import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state_data = pandas.read_csv("50_states.csv")
game = True
count = 0
state_list = []
to_learn = []


def place_state():
    global count
    global game
    if answer == "Exit":
        game = False
    if answer in state_data["state"].values and answer not in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_choice.x), int(state_choice.y))
        t.write(answer)
        count += 1
        state_list.append(answer)
    else:
        print("Try again")


while game:
    print(f"{count} / {len(state_data.state)}")
    answer = screen.textinput(
        title="Enter a State",
        prompt=f"Guess a state: {count} / {len(state_data.state)})",
    ).title()
    state_choice = state_data[state_data.state == answer]
    print(state_list)
    print(answer)
    place_state()
    if count == 50:
        game = False

for state in state_data.state:
    if state in state_list:
        pass
    else:
        to_learn.append(state)

state_df = pandas.DataFrame(to_learn, columns=["States"])
state_df.to_csv("States_to_learn.csv")

screen.exitonclick()
