piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# 0| "a" |1 "b" |2 "c" |3 "d" |4 "e" |5 "f" |6 "g" |7
piano_tuples = ("do", "re", "mi", "fa", "so", "la", "ti")


print(piano_keys[2:5])  # ['c', 'd', 'e']
print(piano_keys[2:])  # ['c', 'd', 'e', 'f', 'g']
print(piano_keys[:5])  # ['a', 'b', 'c', 'd', 'e']
print(piano_keys[2:5:2])  # ['c', 'e']
print(piano_keys[::2])  # ['a', 'c', 'e', 'g']
print(piano_keys[::-1])  # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

print(piano_tuples[2:5])  # ('mi', 'fa', 'so')


