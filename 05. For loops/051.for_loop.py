fruits = ["apple", "peach", "pear"]
for select_fruit in fruits:
    print(select_fruit)  # print all the item in the list one by one till the end
    print(select_fruit + " pie")
    print(fruits)  # print the whole list not just the items
print(fruits[1] + " eye")  # it's not in the loop

# Range() function in for loop
for number in range(1, 10):
    print(number)  # the output is from 1 to 9
for number in range(1, 10, 2):  # the output is 1, 3, 5, 7, 9
    print(number)

# using for loop and range() function to sum all the numbers between 1 and 100
result = 0
for calc in range(1, 101):
    result += calc
print("1-100: ", result)
