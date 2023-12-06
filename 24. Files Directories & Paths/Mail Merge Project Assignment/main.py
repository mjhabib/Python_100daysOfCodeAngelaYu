# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", "r") as names:  # create a list of names from the file
    name_list = names.readlines()
with open("Input/Letters/starting_letter.txt", 'r') as letter:  # open and read the letter text
    letter_text = letter.read()
    for name in name_list:
        stripped_name = name.strip()  # remove '\n' in the list of the names
        # stripped_name = name.replace("\n", '')  # Alternative method: Replace '\n' in the list of the names
        added_name = letter_text.replace("[name]", stripped_name)  # add the names to the letter
        with open(f"Output/ReadyToSend/{stripped_name}.txt", 'w') as done_letter:  # create and save a new file with the name of each person
            done_letter.write(added_name)

