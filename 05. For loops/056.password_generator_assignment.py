import random
print("Welcome to the PyPassword Generator :)")

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))

ran_pass = []
ran_num = random.sample(numbers_list, numbers)
ran_pass.append(ran_num)

ran_sym = random.sample(symbols_list, symbols)
ran_pass.append(ran_sym)

ran_let = random.sample(letters_list, letters)
ran_pass.append(ran_let)

flatList = sum(ran_pass, [])  # turn the nested list into a flat list
str_list = ''.join(flatList)  # join all the characters together as one string
shuffle_pass = random.sample(str_list, letters+symbols+numbers)  # shuffle all the chars
final_result = ''.join(shuffle_pass)  # join them again

print("Here is your password: ", final_result)

# solution #2 - Easy method (no shuffle)
password = ""
for char in range(0, letters):
    password += random.choice(letters_list)

for char in range(0, numbers):
    password += random.choice(numbers_list)

for char in range(0, symbols):
    password += random.choice(symbols_list)

print("Easy S2: ", password)

# hard level - shuffle password
password_list = []
for char in range(0, letters):
    password_list += random.choice(letters_list)

for char in range(0, numbers):
    password_list += random.choice(numbers_list)

for char in range(0, symbols):
    password_list += random.choice(symbols_list)

result = ""
random.shuffle(password_list)
for char in password_list:
    result += char
print("Hard S2: ", result)
