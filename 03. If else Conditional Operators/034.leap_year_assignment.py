print("welcome to the Leap year calculator program.")
leap_year = int(input("Enter any year you want: "))
# must evenly divisible by 4
# and must not evenly divisible by 100
# but if it is, then it must be evenly divisible by 400
# https://bit.ly/36BjS2D
if leap_year % 4 == 0 and leap_year % 100 != 0:
    print("Leap year.")
elif leap_year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")

# solution number 2:
if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")
