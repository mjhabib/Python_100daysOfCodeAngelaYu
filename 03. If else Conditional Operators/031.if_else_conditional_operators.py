print("welcome to the Roller-coaster program :)")
height = int(input("How tall are you in cm? "))
bill = 0
if height >= 120:
    print("Great! You are good to go :)")
    age = int(input("How old are you? "))
    if 55 >= age >= 45:  # Simplified - nested condition
        print("Midlife crisis! You don't need to pay anything!")
    elif age >= 18:
        print("Adults should pay $12.")
        bill = 12
    elif age >= 15:  # I can add as many as elif I want
        print("Teens should pay $10.")
        bill = 10
    else:
        print("Children should pay $8.")
        bill = 8
    photo = input("Do you need a $3 photo too? Answer with N or Y? ")
    if photo == 'Y' or photo == 'y':
        bill += 3
        print(f"Your total payment is ${bill}.")
    else:
        print(f"Your total payment is ${bill}.")
else:
    print("sorry. You need to be taller!")

# = assign something to something else
# == equal to
# != not equal to

# A and B, both have to be True for the statement to be True
# A or B, only one of them need to be True for the statement to be True
# not A, It's reverse a statement, True = False, False = True.
