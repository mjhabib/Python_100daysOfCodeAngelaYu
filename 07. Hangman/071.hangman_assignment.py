import hangman_art  # or 'from hangman_art import logo, stages'
from hangman_words import words  # another way to call something from a module
import random
print(hangman_art.hangman_logo())  # I used a function as an example in this line of code
word_list = words  # 'words' instead of 'hangman_words.words'
chosen_word = random.choice(word_list)
print(f"Cheating word: {chosen_word}")

display = []
word_length = len(chosen_word)
for i in range(word_length):
    # display.append("_")
    display += "_"
print(display)

result = ""
lives = 6
letter = []
end_of_game = False
while not end_of_game and lives != 0:  # while end_of_game == False
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} which means you lose a life :(")
        print(hangman_art.stages[lives])  # I used a list inside a module as an example
    print(display)
    if "_" not in display:
        end_of_game = True
        print(f'Congratulations, you guessed "{result.join(display)}"')
    if lives == 0:
        print("You lose! ")
