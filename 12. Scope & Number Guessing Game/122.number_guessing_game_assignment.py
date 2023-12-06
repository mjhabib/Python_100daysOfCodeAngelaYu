from art import logo
import random

print(logo)
print("I'm thinking a number between 1 and 100 ...\n")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


def attempts():
    if difficulty == 'easy':
        attempt = 10
        return attempt
    else:
        attempt = 5
        return attempt


def random_number():
    number = random.randint(1, 100)
    return number


def compare():
    attempt = attempts()
    number = random_number()
    print(f"Cheating: {number}")
    while attempt != 0:
        print(f"You have {attempt} attempt(s) to guess")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high ")
            attempt -= 1
        elif guess < number:
            print("Too low ")
            attempt -= 1
        else:
            print("That's correct, you won 😊")
            attempt = 0


compare()
