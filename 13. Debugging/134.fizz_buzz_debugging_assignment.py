for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # 'or' was incorrect, we needed an 'and'
        print("FizzBuzz")
    elif number % 3 == 0:  # also here we had another 'if' which was incorrect, we needed an 'elif' instead
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)  # also '[]' around the 'number' was unnecessary
