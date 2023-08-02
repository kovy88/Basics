import os

def sum(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calc():
    num1 = float(input("Jake je 1. cislo? "))

    condition = "ano"
    while condition == "ano":
        for symbol in operations:
            print(symbol)

        user_symbol = input("Zvolte jednu z operaci vyse: ")
        num2 = float(input("Jake je 2. cislo? "))

        result = operations[user_symbol](num1, num2)

        print(f"{num1} {user_symbol} {num2} = {result}")
        condition = input("Napiste ano nebo ne\n")
        if condition == "ano": 
            num1 = result
        elif condition == "ne": 
            os.system("cls")
            calc()
        else: os.system("cls")
calc()