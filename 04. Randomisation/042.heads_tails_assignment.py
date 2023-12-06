import random
rand_int = random.randint(0, 1)
heads_tails = input('What is your choice? "Heads" or "Tails": ')
if rand_int == 0 and heads_tails == 'Heads':
    print('Congratulation. It\'s "Heads".')
elif rand_int == 1 and heads_tails == 'Tails':
    print('Congratulation, it\'s "Tails".')
else:
    print("Sorry. Maybe next time!")
