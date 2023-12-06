# string subscript
print("First letter\n"[0])
print("Second letter"[1])

# Integer
print(123 + 321)
# This is for readability and _ acts as , between numbers
print(123_456_789)

# Float
print(3.14159)

# Boolean
True # Starts with capital letter
False # Starts with capital letter

# Check the type of output
num_char = (len(input("What is your name? ")))
# len function returns an integer value in the output
# print("Your name has " + num_char + " characters.") # Error
print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# another example:
a = 123  # integer
b = str(123)  # string
print(type(a))
print(type(b))

print(23 + float(32.4))
print(23 + float("33.4"))
print(str(100)+str(200))

