logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def operation():
    first = float(input("First Number: "))
    print("Symbols: +, -, *, /")
    calculation = symbols[input("Enter symbol: ")]((first), (float(input("Second: "))))
    return calculation


def operation2():
    print("Symbols: +, -, *, /")
    calculation = symbols[input("Enter symbol: ")](
        (stored_value), (float(input("Second: ")))
    )
    return calculation


symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


stored_value = float()
keep_going = True


while keep_going:
    print(logo)
    stored_value = operation()
    print(stored_value)
    n = input(
        f"\nType 'exit' to quit\n'y' to continue with current value\n'n' to reset to 0\n\nWould you like to continue?\nCurrent value = {
            stored_value
        }\n\n"
    )
    if n == "exit":
        keep_going = False
    while n == "y":
        print(logo)
        print(f" Current value = {stored_value}")
        stored_value = operation2()
        print(stored_value)
        n = input(
            f"\nType 'exit' to quit\n'y' to continue with current value\n'n' to reset to 0\n\nWould you like to continue?\nCurrent value = {
                stored_value
            }\n\n"
        )
        if n == "exit":
            keep_going = False
