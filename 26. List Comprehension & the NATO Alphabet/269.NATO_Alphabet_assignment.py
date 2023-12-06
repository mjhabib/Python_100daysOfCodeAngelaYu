import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {}
for (index, row) in nato_data.iterrows():
    nato_dict.update({row.letter: row.code})

name = input("Enter a name: ").upper()
name_letters = [letter for letter in name]

nato_result = []
for letter in name_letters:
    if letter in nato_dict[letter]:
        nato_result.append(nato_dict[letter])

print(nato_result)


# or simpler version:
output_list = [nato_dict[letter] for letter in name]

print(f"\n{output_list}")
