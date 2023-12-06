def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}


# short version:
def calculator():
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    wanna_continue = True
    while wanna_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        repeat = input(f"Wanna continue with '{answer}'? Type 'y' to continue or 'n' to exit or 'r' to reset: ")
        if repeat == 'r':
            calculator()  # Recursion == endless calculation
        elif repeat == 'y':
            num1 = answer
        elif repeat == 'n':
            wanna_continue = False


calculator()  # Recursion == endless calculation


# long version:
# num1 = float(input("What's the first number? "))
# for symbol in operations:
#     print(symbol)
# operation_symbol = input("Pick an operation: ")
# num2 = float(input("What's the second number? "))
#
# calc_function = operations[operation_symbol]
# first_answer = calc_function(num1, num2)
#
# print(f"{num1} {operation_symbol} {num2} = {first_answer}")
#
# wanna_continue = True
# while wanna_continue:
#     repeat = input("\nDo you want to continue? Type 'y' or 'n': ")
#     if repeat == 'n':
#         wanna_continue = False
#         print("Thank you baby :)")
#     else:
#         operation_symbol = input("Pick another operation: ")
#         num3 = int(input("What's the next number? "))
#         calc_function = operations[operation_symbol]
#         second_answer = calc_function(first_answer, num3)
#
#         print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
