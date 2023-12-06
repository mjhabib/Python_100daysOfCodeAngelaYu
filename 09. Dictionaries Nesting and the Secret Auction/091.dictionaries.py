programming_dictionaries = {
    "bug": "An error in programming that prevents program from running as expected.",
    "function": "A piece of code that you can easily call over and over again.",
    "loop": "The action of doing something over and over again.",  # key: value
    123: "Another type of data which is a number.",
}  # the last comma is optional
empty_dict = {}

# retrieving data from dict
print(programming_dictionaries["bug"])  # calling a key from dictionary
print(programming_dictionaries[123])  # calling a key number

# adding items to the dict
empty_dict["test"] = "This is just a test for adding new item to a dict"
print(empty_dict)

# wipe an existing dict
empty_dict = {}
print(f"There is nothing here: {empty_dict}")

# edit an item in a dict
programming_dictionaries["bug"] = "I'm changing the definition of bug in our dict"
print(programming_dictionaries["bug"])

# looping through a dict
print("Loop through our dict")
for key in programming_dictionaries:
    print(key)  # print just keys
    print(programming_dictionaries[key])  # print the value of a key in our dict
