print("Welcome to the FizzBuzz game :)")
for numbers in range(1, 101):
    if numbers % 3 != 0 and numbers % 5 != 0:
        print(numbers)
    elif numbers % 3 == 0 and numbers % 5 != 0:
        print("Fizz")
    elif numbers % 5 == 0 and numbers % 3 != 0:
        print("Buzz")
    elif numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")

# solution #2 order of divisible is important in this challenge
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("S2: FizzBuzz")
    elif number % 3 == 0:
        print("S2: Fizz")
    elif number % 5 == 0:
        print("S2: Buzz")
    else:
        print("S2: ", number)

