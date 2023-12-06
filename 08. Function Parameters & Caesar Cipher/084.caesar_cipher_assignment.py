alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: "))


def encrypt(message, key):
    pointer1 = -1
    pointer2 = -1
    pointer3 = -1
    letters_position = []  # to save the position of each original char
    cipher_position = []  # to save the position of each cipher char
    cipher_list = []  # to save the encrypted chars
    # cipher_message = ""  # to save the encrypted message
    message_list = [i for i in message]  # str to a list of chars

    for i in message_list:  # create a list of all the chars' position
        pointer1 += 1
        if message_list[pointer1] in alphabet:
            letters_position.append(alphabet.index(i))
    print("original", letters_position)

    for i in letters_position:  # shift all the chars' position
        pointer2 += 1
        cipher_position.append(letters_position[pointer2]+key)
    print("cipher", cipher_position)

    for i in cipher_position:  # print the encrypted message
        pointer3 += 1
        x = cipher_position[pointer3]
        cipher_list.append(alphabet[x])
    cipher_message = "".join(cipher_list)

    print("Here is your encrypted message: ", cipher_message)


def decrypt():
    print("Here is your decrypted message: ")


if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt()
else:
    print("You typed an incorrect input! Try again.")
