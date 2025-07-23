import random

import art
import game_data


def format_data(account):
    return f"{account['name']} a {account['description']} from {account['country']}"


def display_game(a, b, score):
    print(art.logo)
    print(f"Your current score is {score}\n\n")
    print(f"A: {format_data(a)}")
    print(art.vs)
    print(f"B: {format_data(b)}")


def check_answer(a, b):
    if a["follower_count"] < b["follower_count"]:
        return "b"
    else:
        return "a"


def main():
    game = True
    score = 0
    choice_a = random.choice(game_data.data)

    while game:
        choice_b = random.choice(game_data.data)

        while choice_a == choice_b:
            choice_b = random.choice(game_data.data)

        display_game(choice_a, choice_b, score)

        answer = check_answer(choice_a, choice_b)
        guess = input("\n\nWho has more followers? 'A' or 'B' ").lower()
        while guess not in ["a", "b"]:
            guess = input("Invalid input. Please type 'A' or 'B': ").lower()
        if guess == answer:
            print("Correct")
            score += 1
            choice_a = choice_b
        else:
            print("Incorrect")
            game = False
        print("\n" * 20)
        print(f"Your final score is {score}")


main()
