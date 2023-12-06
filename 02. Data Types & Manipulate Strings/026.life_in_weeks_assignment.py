age = input("How old are you? ")
years_left = 90-int(age)
days = years_left*365
weeks = days/7  # or years_left * 52 >> which does not need to be round
months = days//30  # or years_left * 12 >> which does not need to be round
print(f"You have {days} days, {round(weeks)} weeks, and {months} months left.")
