print("welcome to BMI calculator version 2.0")
weight = float(input("How much weight (in Kg) do you have? "))
height = float(input("How tall (in meter) are you? "))
result = weight / height ** 2
if result <= 18.5:
    # \033[1m == bold
    print(f"Your BMI is {round(result)}, you are\033[1m underweight.")
elif result <= 25:
    print(f"Your BMI is {round(result)}, you have a\033[1m normal weight.")
elif result <= 30:
    print(f"Your BMI is {round(result)}, you are\033[1m slightly overweight.")
elif result <= 35:
    print(f"Your BMI is {round(result)}, you are\033[1m obese.")
else:
    print(f"Your BMI is {round(result)}, you are\033[1m clinically obese.")
