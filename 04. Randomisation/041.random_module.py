# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
import random
# this is how modules work
import my_pi_module
print(my_pi_module.pi)  # 3.14159246

# print a random integer between 10 and 100
random_int = random.randint(10, 100)
print(random_int)

# print a float random number between 0 and 1
random_float = random.random()
print(random_float)
print("A random floating number by multiplying it to another number: ", random_float*5)
print("A random floating number between 1 and 5: ", random.uniform(1, 5))
