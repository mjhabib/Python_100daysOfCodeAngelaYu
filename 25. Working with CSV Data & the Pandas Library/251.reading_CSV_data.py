# old way
with open("weather_data.csv") as file1:
    raw_data = file1.readlines()
    print(f"Raw data: {raw_data}\n")
    stripped_data = []
    for data in raw_data:
        stripped_data.append(data.strip())
    print(f"Stripped data: {stripped_data}\n")


# another way (faff):
import csv

with open("weather_data.csv") as file2:
    data = csv.reader(file2)
    print(f"Data Object: {data}\n")
    for row in data:
        print(f"Each row: {row}")

# assignment
with open("weather_data.csv") as data_file:
    data_object = csv.reader(data_file)
    temperature = []
    for row in data_object:
        if row[1] != 'temp':  # remove 'temp' in first row from our list
            temperature.append(int(row[1]))
    print(f"\nOnly temperature items: {temperature}")

# another longer way for this assignment:
with open("weather_data.csv") as data_file:
    data_object = csv.reader(data_file)
    temperature = []
    int_temperature = []
    for row in data_object:
        temperature.append(row[1])
        # slice does not work on objects, that's why we need another for loop to convert our object into a list
    for tmp in temperature[1:]:
        int_temperature.append(int(tmp))
    print(f"\nAll items in temperature: {temperature}")
    print(f"\nOnly int items in temperature: {int_temperature}\n")


# the power of pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data['temp'])



