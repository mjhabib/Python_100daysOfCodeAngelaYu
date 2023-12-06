print('Welcome to the "Tip Calculator" ')
check = input("What was the total bill? $")
tip = input("Type the percentage of tip do you wanna pay? %")
split = input("How many people to split the bill? ")
percentage = float(check) * float(tip) / 100 / float(split)
# another way: tip / 100 * check + check
# or: check * (1 + tip / 100)
percentage += float(check) / float(split)
# final_amount = round(percentage, 2)
final_amount = "{:.2f}".format(percentage)  # Ex: $12.60 instead of $12.6
print(f"Each person should pay ${final_amount}")
