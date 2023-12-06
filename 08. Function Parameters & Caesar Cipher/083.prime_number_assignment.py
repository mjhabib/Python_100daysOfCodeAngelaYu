def prime_checker(prime):
    counter = 0
    length = prime
    for i in range(prime):
        if prime % length == 0:
            counter += 1
        length -= 1
    if counter == 2:
        print(f'"{prime}" is a prime number.')
    else:
        print(f'"{prime}" is NOT a prime number.')


n = int(input("Check this number: "))
prime_checker(n)
# Prime numbers are numbers that can only be cleanly (no remainder) divided by themselves and 1.
# For example, '7' is prime because it can be divided to '1' and '7', but '4' is not a prime because it can be divided not only to '1' and '7' but also to '2'

# solution #2
number = int(input("Type a number: "))
is_prime = True
# we know any number will divisible by 1 and itself that's why the range starts from 2 to a number before itself
for j in range(2, number):
    if number % j == 0:
        is_prime = False
if is_prime:
    print("Prime")
else:
    print("Not prime")
