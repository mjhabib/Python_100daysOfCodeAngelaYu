from ceasar_cipher_logo import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# the easiest way to solve the out of range error if we have a letter towards the end of the list and wanted to shift it further, but we didn't have any alphabet left!
should_continue = True
while should_continue:
    # to ask user if she/he wants to re-run the program again

    direction = input("Type 'encode' or 'decode': ")
    text = input("Type message: \n").lower()
    shift = int(input("Type the key code: "))
    shift = shift % 26
    # just in case user wants to enter a large number, ex: 45 % 26 = 19, now we don't get an out of range error

    # short version #1
    def ceasar(direct, plain_text, shift_amount):
        cipher_text = ""
        new_position = 0
        for char in plain_text:
            if char in alphabet:  # we don't want to cipher any chars other than the letters
                position = alphabet.index(char)
                if direct == 'encode':
                    new_position = position + shift_amount
                elif direct == 'decode':
                    new_position = position - shift_amount
                else:
                    print("Your input is wrong! ")
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += char  # we don't want to lose any char the user might type
        print(f"Output:  '{cipher_text}'")


    # short version #2
    # def ceasar(direct, plain_text, shift_amount):
    #     end_text = ""
    #     if direct == 'decode':
    #         shift_amount *= -1
    #     for letter in plain_text:
    #         position = alphabet.index(letter)
    #         new_position = position + shift_amount
    #         end_text += alphabet[new_position]
    #     print(f"The {direct}d text is {end_text}")

    ceasar(direct=direction, plain_text=text, shift_amount=shift)
    # or - ceasar(direction, text, shift)

    # end of our while loop to see if the user wants to play or not
    repeat = input(f"Type 'yes' if you want to go again, 'no' if you don't: ")
    if repeat == 'no':
        should_continue = False
        print("Have a good day :)")

# long version
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print("Output: ", cipher_text)
#
#
# def decrypt(plain_text, shift_amount):
#     decipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decipher_text += new_letter
#     print("Output: ", decipher_text)
#
#
# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == 'decode':
#     decrypt(text, shift)
# else:
#     print("You typed an incorrect input! Try again.")
