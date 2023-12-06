import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))  # 'DataFrame' = equivalent to tables in 'sheets' or 'excel' files
print(type(data['temp']))  # 'Series' = equivalent to a list or a single column in a excel file

data_dict = data.to_dict()  # converting data to a dict
print(f"\nDict:  {data_dict}")

temp_list = data['temp'].to_list()   # converting data to a list
print(f"\nList: {temp_list}\n")

# calculate average assignment
total = 0
for i in temp_list:
    total += i
avg = total / len(temp_list)
print(f"Avg: {avg}")

# or simply by using the sum() function
print(f"Sum: {sum(temp_list) / len(temp_list)}")

# or by using pandas
print(f"Pandas mean: {data['temp'].mean()}")

print(f"Pandas max: {data['temp'].max()}")

# get data in columns using pandas
print(data["condition"])  # treating it like a dict
# or
print(data.condition)  # treating it like an object

# get a data row using pandas
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp[0])
monday_temp_f = monday_temp * 9/5 + 32  # converting Celsius into Fahrenheit
print(monday_temp_f)

# create a DataFrame from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65],
}

students_data = pandas.DataFrame(data_dict)
print(students_data)
students_data.to_csv("students_data.csv")


