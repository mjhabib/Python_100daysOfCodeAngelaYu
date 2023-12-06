# # functions can have input/output/functionality
def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


# # first-class objects can be passed around as arguments like, int/str/float/etc...
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(divide, 8, 2)
print(result)  # 4.0


# # nested functions
def outer_fun():
    print("I'm outer")

    def inner_fun():
        print("I'm inner")

    inner_fun()


# because the inner function is nested inside the outer function, I can't have access to it here unless I called it inside my outer function
outer_fun()  # I'm outer  \n  I'm inner


# # functions can be returned from other functions
def new_outer_fun():
    print("I'm outer")

    def new_inner_fun():
        print("I'm inner")

    return new_inner_fun()


# this is how I can call a nested function
nested_function = new_outer_fun()  # I'm outer
nested_function  # I'm inner


# # function decorator
import time


def delay_decorator(function):
    def wrapper_fun():
        time.sleep(2)
        # do something before
        function()
        # do something after

    return wrapper_fun()


def say_hello():  # print hello immediately
    print(f"\n")
    print("Hello baby")


say_hello()


@delay_decorator  # also known as syntactic sugar!
def say_bye():  # print bye after 2-sec delay
    print(f"Bye sugar\n")


# if I didn't want to shorten my code using this syntactic sugar, my code would look like this:
nested_decorator = delay_decorator(say_hello)  # with 2-sec delay
nested_decorator
