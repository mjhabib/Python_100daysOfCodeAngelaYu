print(8 / 3)  # 2.6666666666666665
print(round(8 / 3))  # 3
print(round(8 / 3, 2))  # 2.67
print(8 // 3)  # 2 >> when I don't want to convert it, but I want a whole number

result = 4 / 2  # 2
result /= 2  # 2/2=1 >> result = result / 2 (*=, +=, -=)
print(result)  # 1

# f-strings
a_int = 10
b_float = 12.5
c_boolean = True
print("The hard way: " + str(a_int) + ", " + str(b_float) + ", " + str(c_boolean))
# this is the better way
print(f"The easy way: {a_int}, {b_float}, {c_boolean}")
