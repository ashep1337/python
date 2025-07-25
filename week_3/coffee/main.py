from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
make = CoffeeMaker()
money = MoneyMachine()

on = True

while on:
    options = menu.get_items()
    choice = input(f"What would you like to drink {options}")

    if choice == "off":
        on = False
    elif choice == "report":
        make.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        count = money.make_payment(drink.cost)

    if make.is_resource_sufficient(drink) and count:
        make.make_coffee(drink)
