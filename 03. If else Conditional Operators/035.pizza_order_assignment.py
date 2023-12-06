print("Welcome to the Pizza Order program :)")
size = input("What kind of pizza do you want? S = Small, M = Medium, L = Large? ")
bill = 0
if size == 'S' or size == "s":
    print("Great! Small pizzas are $15 each.")
    bill = 15
    pepperoni = input("Do you want pepperoni too? Y = Yes, N = No? ")
    if pepperoni == 'Y' or pepperoni == 'y':
        print("Nice! Pepperoni for a Small Pizza is $2.")
        bill += 2
    cheese = input("Do you want extra cheese too? Y = Yes, N = No? ")
    if cheese == 'Y' or cheese == 'y':
        print("Good choice! Extra cheese is $1.")
        bill += 1
    print(f"Thank you. You total is ${bill}.")

elif size == 'M' or size == "m":
    print("Great! Medium pizzas are $20 each.")
    bill = 20
    pepperoni = input("Do you want pepperoni too? Y = Yes, N = No? ")
    if pepperoni == 'Y' or pepperoni == 'y':
        print("Nice! Pepperoni for a Medium Pizza is $3.")
        bill += 3
    cheese = input("Do you want extra cheese too? Y = Yes, N = No? ")
    if cheese == 'Y' or cheese == 'y':
        print("Good choice! Extra cheese is $1.")
        bill += 1
    print(f"Thank you. You total is ${bill}.")

elif size == 'L' or size == "l":
    print("Great! Large pizzas are $25 each.")
    bill = 25
    pepperoni = input("Do you want pepperoni too? Y = Yes, N = No? ")
    if pepperoni == 'Y' or pepperoni == 'y':
        print("Nice! Pepperoni for a Large Pizza is $3.")
        bill += 3
    cheese = input("Do you want extra cheese too? Y = Yes, N = No? ")
    if cheese == 'Y' or cheese == 'y':
        print("Good choice! Extra cheese is $1.")
        bill += 1
    print(f"Thank you. You total is ${bill}.")

else:
    print("Sorry that we don't have what you want!")

