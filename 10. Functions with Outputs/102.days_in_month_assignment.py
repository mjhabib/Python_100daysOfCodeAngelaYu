def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month > 12 or month < 1 or year < 1:  # to make sure the user enters the right month/year
        return "Invalid month/year"

    if is_leap(year) == True and month == 2:  # or "is_leap(year)" # no need to mention the "== True"
        return month_days[1] + 1  # or simply "return 29"
    else:
        return month_days[month - 1]  # list starts from '0'


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
