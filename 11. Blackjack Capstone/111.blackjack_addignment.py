import random
from blackjack_art import logo

# Our BlackJack house rules:
# The deck is unlimited in size
# The Jack/Queen/King all count as 10
# The Ace can count as either 11 or 1
# Sample online game: https://games.washingtonpost.com/games/blackjack/


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the calculated score from the cards"""
    # if 11 in cards and 10 in cards and len(cards) == 2:  # blackjack
    if sum(cards) == 21 and len(cards) == 2:  # short version
        return 0  # zero represents blackjack
    if 11 in cards and sum(cards) > 21:  # replace ace (11) with 1 if the cards are over 21
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw 🙃"
    elif user_score == 0:
        return "You have a BlackJack, you won 🤩"
    elif computer_score == 0:
        return "Computer has a BlackJack, you lose 😤"
    elif user_score > 21:
        return "You went over 21, you lose 😠"
    elif computer_score > 21:
        return "Computer went over 21, it loses 😊"
    elif user_score > computer_score:
        return "You win 😍"
    else:
        return "You lose 😑"


def play_again():  # to start our game over and over
    print(logo)

    is_game_over = False
    user_cards = []
    computer_cards = []
    for _ in range(2):
        # new_card = deal_card()
        # user_cards.append(new_card)
        user_cards.append(deal_card())  # short version of two lines of code above
        computer_cards.append(deal_card())
        # we can't use '+=' for the line code above because 'new_card' is not a list, and we get a "TypeError iterable"
        # '+=' operation is another way of using 'extend' function which works on lists

    while not is_game_over:  # this is how user will play
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to deal another card or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:  # this is how computer will play
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" \nYour final hand: {user_cards}, Final score: {user_score}")
    print(f" \nComputer final hand: {computer_cards}, Final score: {computer_score}\n")
    print(compare(user_score, computer_score))


while input("Do you wanna play the game of BlackJack? Type 'y' or 'n': ") == 'y':
    play_again()
