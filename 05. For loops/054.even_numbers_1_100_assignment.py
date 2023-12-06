result = 0
for even_numbers in range(0, 101, 2):
    result += even_numbers
print(result)

# solution #2
total = 0
for even_numbers in range(1, 101):
    if even_numbers % 2 == 0:
        total += even_numbers
print(total)
