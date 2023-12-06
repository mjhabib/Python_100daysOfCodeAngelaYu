# list of all America's states in order of joining the union
us_states_in_order = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina" "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(us_states_in_order[2])  # show me the third state from the beginning
print(us_states_in_order[-3])  # show me the third state backward
us_states_in_order[3] = "New Georgia!"  # Altered item in the list
print(us_states_in_order[3])
us_states_in_order.append("MJ City")  # Add a new item to the list
print(us_states_in_order[49])
us_states_in_order.extend(["City1", "City2", "City3"])  # Add a list of items to our previews list
print("\nExtend: ", us_states_in_order[50:52])

print("\nNew method: ")
from operator import itemgetter
print(*itemgetter(50, 51, 52)(us_states_in_order))
print("\nOr: ", itemgetter(50, 51, 52)(us_states_in_order))

num_states = len(us_states_in_order)  # numbers of items in a list
print("\nLast item (-1): ", us_states_in_order[num_states - 1])  # -1 because our list starts at 0

fruits = ["Apple", "Banana", "Apricot", "Papaya", "Peach", "Pomegranate", "Pineapple", "Raspberries", "Strawberries", "Tangerine", "Watermelon"]
vegetables = ["Potato",	"Capsicum",	"Tomato", "Green peas", "Apple gourd", "Onion", "Cauliflower"]
nested_list = [fruits, vegetables]
print("\nWhole nested list: ", nested_list)
print("\nList #1, Item #2 (We have two lists, 0 and 1)", nested_list[1][2])


nested_lists = ['0', '1', '2', ['3', '4', '5'], '6', ['7', '8', '9']]
print("\nNegative indexing: ", nested_lists[-3][-1])  # = 5
# negative indexing : if we count backwards, sublist #3 and item #1 means 5

print("\nPositive indexing: ", nested_lists[5][1])  # = 8
# positive indexing : last sublist, second item

# another example:
geeksforgeeks = [10, 20, 30, 40, [80, 60, 70]]

# Printing sublist at index 4
print(geeksforgeeks[4])  # [80, 60, 70]

# Printing 1st element of the sublist
print(geeksforgeeks[4][0])  # 80

# Printing 2nd element of the sublist
print(geeksforgeeks[4][1])  # 60

# Printing 3rd element of the sublist
print(geeksforgeeks[4][2])  # 70


