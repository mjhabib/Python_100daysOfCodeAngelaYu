import random

rand_num = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors? "))
if user_choice == 0:
    print("You chose Rock\n" + r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    if rand_num == 0:
        print("Lucky! Computer chose Rock too, play again.\n" + r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    if rand_num == 1:
        print("Sorry. Computer chose Paper, you lost :( \n" + r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
    if rand_num == 2:
        print("Congratulations. Computer chose Scissors, you won :)\n" + r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

if user_choice == 1:
    print("You chose Paper\n" + r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
    if rand_num == 0:
        print("Congratulations. Computer chose Rock, you won :)\n" + r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    if rand_num == 1:
        print("Lucky! Computer chose Paper too, play again.\n" + r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
    if rand_num == 2:
        print("Sorry. Computer chose Scissors, you lost :( \n" + r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

if user_choice == 2:
    print("You chose Scissors\n" + r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
    if rand_num == 0:
        print("Sorry. Computer chose Rock, you lost :( \n" + r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    if rand_num == 1:
        print("Congratulations. Computer chose Paper, you won :)\n" + r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
    if rand_num == 2:
        print("Lucky! Computer chose Scissors too, play again.\n" + r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
# else:
#     print("You chose an invalid number, so you lost!")
# I could put all the ascii images inside a list and use them in my program instead of coping and pasting
