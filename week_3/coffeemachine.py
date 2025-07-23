import time

logo_coffee = r"""

      ( (
      ) )
   ........
   |      |]
   \      /
    `----'
"""
logo_coin = r"""

        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \
  /`       .-'~"-.       `\
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;  INGODWE /      \\)P    ;
  \  TRUST '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
"""

logo_start = r"""
 .--.    .-..-.         .                .
:        |  |           |                |
|    .-.-|--|-.-. .-.   |--. .-. .--..-. |
:   (   )|  |(.-'(.-'   |  |(.-' |  (.-' '
 `--'`-' '  ' `--'`--'  '  `-`--''   `--'o

"""
logo_water = r'''

 .-'"""`-.
(         )
|`-.___.-'|
|.-'"""`-.|
|         |
|`-.___.-'|
|         |
|. ' " ` .|
|         |
 `-.___.-'
'''

logo_milk = r"""
     _____
    j_____j
   /_____/_\
   |_(~)_| |
   | )"( | |
   |(@_@)| |
   |_____|,'
"""

logo_beans = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣷⡄⠀⠙⢿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣦⡀⠀⠙⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣦⣄⠀⠈⠛⠿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠘⢿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠘⢁⣴⣾⣿⡿⠋⠀⠀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⠇⢀⣶⣿⣿⣿⠋⠀⢀⣤⣾⣷⠀⠀
⠀⠀⠀⠀⠠⠤⠶⣶⣤⣄⣉⠙⠿⣿⡿⠃⣰⣿⣿⣿⣿⠃⠀⢰⣿⣿⣿⣿⡇⠀
⠀⠀⣤⣤⣤⣄⡀⠈⠻⣿⣿⣷⣦⡈⠁⣼⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠃⠀
⠀⢸⣿⣿⣿⣿⣷⠀⠀⢹⣿⣿⣿⣷⡀⢻⣿⣿⣿⣿⣿⠀⠀⢹⣿⣿⣿⡟⠀⠀
⠀⠘⣿⣿⣿⣿⣿⣇⠀⠈⠻⣿⣿⣿⣷⠀⣿⣿⣿⣿⠟⠀⠀⣾⣿⣿⡟⠀⠀⠀
⠀⠀⠙⣿⣿⣿⣿⣿⣦⣀⠀⠀⠉⠛⠻⠀⣿⡿⠟⠁⠀⣠⣾⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣶⣶⠄⠀⠈⠋⠀⢀⣠⣾⡿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")


def coin_count(price):
    total = 0
    print(f"You owe: {price}")
    while total < price:
        quarters = int(get_float_input("Quarters: ")) * 0.25
        dimes = int(get_float_input("Dimes: ")) * 0.10
        nickels = int(get_float_input("nickels: ")) * 0.05
        pennies = int(get_float_input("Pennies: ")) * 0.01
        total += round(quarters + dimes + nickels + pennies, 2)
        print(f"Your current total is: {total}\nThe price is {price}")

    if total > price:
        refund = round(total - price, 2)
        print("Getting you change.")
        time.sleep(2)
        print(logo_coin)
        print(f"Here is your change: {refund}")
        time.sleep(2)

    return True


def refill(item):
    resources[item] += 100


def coffee_picker(choice):
    if resources["water"] - MENU[choice]["ingredients"]["water"] < 0:
        while resources["water"] - MENU[choice]["ingredients"]["water"] < 0:
            print("Not enough water")
            print("refilling water")
            time.sleep(2)
            print(logo_water)
            refill("water")

    if resources["coffee"] - MENU[choice]["ingredients"]["coffee"] < 0:
        while resources["coffee"] - MENU[choice]["ingredients"]["coffee"] < 0:
            print("Not enough coffee")
            print("refilling coffee")
            time.sleep(2)
            print(logo_beans)
            refill("coffee")

    if "milk" in MENU[choice]["ingredients"]:
        if resources["milk"] - MENU[choice]["ingredients"]["milk"] < 0:
            while resources["milk"] - MENU[choice]["ingredients"]["milk"] < 0:
                print("Not enough milk")
                print("refilling milk")
                time.sleep(2)
                print(logo_milk)
                refill("milk")

    return True


def serve(cofefe):
    print("Brewing....")
    time.sleep(1)
    print("Dispensing coffee")
    time.sleep(2)
    print(logo_coffee)
    print(f"Here is your {cofefe}!")
    time.sleep(2)
    resources["water"] -= MENU[cofefe]["ingredients"]["water"]
    resources["coffee"] -= MENU[cofefe]["ingredients"]["coffee"]
    if "milk" in MENU[cofefe]["ingredients"]:
        resources["milk"] -= MENU[cofefe]["ingredients"]["milk"]


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


active = True


while active:
    print(logo_start)
    coffee_type = input("What would you like?: 'espresso/cappuccino/latte' ")

    if coffee_type == "off":
        active = False
        break

    if coffee_type == "report":
        print_report()
        continue

    if coffee_type == "refill":
        refill(input("What would you like to refill?"))
        continue

    if coffee_type not in MENU:
        print("Invalid option")
        continue

    #    active = coffee_picker(coffee_type)
    #
    #    if not active:
    #        print("Machine inactive due to low resources.")
    #        break

    if coffee_picker(coffee_type):
        if coin_count(MENU[coffee_type]["cost"]):
            serve(coffee_type)
    profit += MENU[coffee_type]["cost"]
