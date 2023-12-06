import datetime as dt

current_data_time = dt.datetime.now()
print(current_data_time)  # 2023-07-15 17:11:15.556298  = datetime object

current_year = current_data_time.year
if current_year == 2023:
    print(current_year)  # 2023 = int


day_of_week = current_data_time.weekday()
print(day_of_week)  # 5 = Saturday, because it counts from zero


my_birthday = dt.datetime(year=1991, month=1, day=27)
print(my_birthday)  # 1991-01-27 00:00:00  -  I can also specify the hour/min/sec
