# Describe Problem
def my_function():
    for i in range(1, 21):  # originally it was 20 and the range starts at 0 and ends at 19
        if i == 20:
            print("You got it")


my_function()

# Reproduce the Bug
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # originally it was a number (1, 6) and our list starts from 0-5 - 6 == out-of-range error
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth? "))
if 1980 < year < 1994:
    print("You are a millennial.")
elif year >= 1994:  # originally it was "year > 1994" that's why the year 1994 was not included
    print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?"))  # originally we didn't turn the age into integer
if age > 18:
    print(f"You can drive at age {age}.")  # also we needed to turn this statement into an f-string

# Print is Your Friend
pages = 0  # this line of code is useless
word_per_page = 0  # this line of code is useless
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))  # originally it has a '==' sign which means evaluated, not '=' sign which means assignment
total_words = pages * word_per_page
print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # originally a tab (indent) was missed here that's why the print only returns one item (the last one)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
