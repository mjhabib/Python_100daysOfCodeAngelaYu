import pandas

data = pandas.read_csv("squirrels_census_data.csv")

# old way:
# gray = 0
# black = 0
# cinnamon = 0
# others = 0
# species_color = data["Primary Fur Color"]
# for count in species_color:
#     if count == "Gray":
#         gray += 1
#     elif count == "Cinnamon":
#         cinnamon += 1
#     elif count == "Black":
#         black += 1
#     else:
#         others += 1

# new way using pandas:
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray, cinnamon, black],
}

final_count = pandas.DataFrame(color_dict)
final_count.to_csv("squirrels_final_count.csv")
print(final_count)
