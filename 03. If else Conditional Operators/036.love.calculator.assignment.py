print("Welcome to the Love Calculator program ;) ")
your_name = input("What is your name? ").lower()
lovers_name = input("What is your lover's name? ").lower()
t = your_name.count('t')
r = your_name.count('r')
u = your_name.count('u')
e = your_name.count('e')
t1 = lovers_name.count('t')
r1 = lovers_name.count('r')
u1 = lovers_name.count('u')
e1 = lovers_name.count('e')
l2 = your_name.count('l')
o2 = your_name.count('o')
v2 = your_name.count('v')
e2 = your_name.count('e')
l3 = lovers_name.count('l')
o3 = lovers_name.count('o')
v3 = lovers_name.count('v')
e3 = lovers_name.count('e')
sum_true = t + r + u + e + t1 + r1 + u1 + e1
sum_love = l2 + o2 + v2 + e2 + l3 + o3 + v3 + e3
combine = str(sum_true) + str(sum_love)
score = int(combine)
if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
