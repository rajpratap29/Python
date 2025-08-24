from art import logo
import os

def clear():
    os.system('clear')

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def mul(n1, n2):
    return n1 * n2

# Divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pickup an operation : ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num2} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()