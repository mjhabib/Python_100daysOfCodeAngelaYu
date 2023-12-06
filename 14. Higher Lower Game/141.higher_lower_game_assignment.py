from random import choice
from art import logo, vs_tag
from game_data import data


def gen_name_a():
    """Return our first random name from dictionary"""
    return choice(data)


def gen_name_b():
    """Return our second random name from dictionary"""
    return choice(data)


def random_name_a():
    """Save our first random name apart from its followers into separate variables, so we can use them later"""
    first_name = gen_name_a()
    global score_a
    score_a = int(first_name['follower_count'])
    compare_a = f"Compare A: {first_name['name']}, a/an {first_name['description']}, from {first_name['country']}"
    return compare_a


def random_name_b():
    """Save our second random name apart from its followers into separate variables, so we can use them later"""
    second_name = gen_name_b()
    global score_b
    score_b = int(second_name['follower_count'])
    compare_b = f"Against B: {second_name['name']}, a/an {second_name['description']}, from {second_name['country']}\n"
    return compare_b


counter = 0
was_correct = True


def a_vs_b():
    """Compare if our first name has more followers than the second one"""
    if score_a > score_b:
        global counter
        counter += 1
        print(f"Correct, '{score_a}M' vs '{score_b}M', your current score: '{counter}'\n")
    else:
        print(f"Sorry, '{score_a}M' vs '{score_b}M', here is your final score: '{counter}'\n")
        global was_correct
        was_correct = False


def b_vs_a():
    """Compare if our second name has more followers than the first one"""
    if score_a < score_b:
        global counter
        counter += 1
        print(f"Correct, '{score_a}M' vs '{score_b}M', your current score: '{counter}'\n")
    else:
        print(f"Sorry, '{score_a}M' vs '{score_b}M', here is your final score: '{counter}'\n")
        global was_correct
        was_correct = False


print(logo)
saved_name_a = random_name_a()  # we don't want to lose our data if our first name has more followers
saved_name_b = random_name_b()  # we don't want to lose our data if our second name has more followers
while was_correct:

    if saved_name_a == saved_name_b:  # to prevent getting two exact names
        saved_name_a = random_name_a()

    print(saved_name_a)
    print(vs_tag)
    print(saved_name_b)

    user_choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    if user_choice == 'a':
        a_vs_b()
        saved_name_b = random_name_b()
    elif user_choice == 'b':
        b_vs_a()
        saved_name_a = random_name_a()
    else:
        print("\nYour input was incorrect. Type 'A' or 'B': ")
