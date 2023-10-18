from calculator_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("Whats the first number? "))
    for symbol in operations:
        print(symbol)

    keep_calculating = True

    while keep_calculating:
        operation_symbol = input("Pick a math opertaion: ")
        new_number = float(input("What's the next number? "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, new_number)
        print(f"{num1} {operation_symbol} {new_number} = {answer}")

        if (
            input(
                f"Would you like to keep calculating with {answer}? 'y' to continue or 'n' to start over : "
            )
            == "y"
        ):
            num1 = answer
        else:
            keep_calculating = False
            calculator()


calculator()
