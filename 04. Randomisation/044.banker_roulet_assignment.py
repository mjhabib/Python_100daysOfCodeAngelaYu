import random
names_string = input("Please enter the names follow by a comma, Ex: Name1, Name2: ")
# in this stage we have a string of names NOT a list of names to work on
names = names_string.split(",")
# It breaks down a bigger string into smaller ones by a comma and makes a list
count_names = len(names)  # we need to know the number of our names
random_person_int = random.randint(0, count_names-1)
# -1 is because the len() function starts from 1 but our list starts from 0
print(f"{names[random_person_int]} is going to pay the bill today.")

# Also the easiest method for this is to use the "choice()" function
who_will_pay = random.choice(names)
print(who_will_pay + " is not lucky today.")
