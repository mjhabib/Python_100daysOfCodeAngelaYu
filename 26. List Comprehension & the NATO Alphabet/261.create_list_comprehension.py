# old-fashion way:
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# the better way using list comprehension
# new_list = [new_item for item in list]
another_new_list = [m + 1 for m in numbers]

print(f"{new_list} vs {another_new_list}\n")  # [2, 3, 4] vs [2, 3, 4]

# list comprehension is not limited to lists only!
# we can also use other sequences like 'strings', 'tuples', 'dicts' 'ranges', etc ...
name = "MJ Habib"
new_letter = [letter for letter in name]
print(f"{new_letter}\n")  # ['M', 'J', ' ', 'H', 'a', 'b', 'i', 'b']

new_range = [n * 2 for n in range(1, 5)]
print(new_range)  # [2, 4, 6, 8]

# conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["MJ", "Saeed", "Omid", "Hasan", "Taghi", "Jose"]
short_names = [i for i in names if len(i) < 5]
print(short_names)  # ['MJ', 'Omid', 'Jose']

long_names = [i.upper() for i in names if len(i) > 4]
print(long_names)  # ['SAEED', 'HASAN', 'TAGHI']
