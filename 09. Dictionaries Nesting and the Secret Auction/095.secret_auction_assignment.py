bidders_dict = {}

more_bidders = True
while more_bidders:
    names = input("What is your name? ")
    price = int(input("How much do you want to bid? $"))
    bidders_dict[names] = price

    if input("Are there any more bidders? 'yes' or 'no'? ") == 'yes':
        more_bidders = True
    else:
        more_bidders = False

highest_bid = 0
winner = ""
for bidder in bidders_dict:
    bid_amount = bidders_dict[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f" The winner is '{winner}' with the bid of '${highest_bid}'")
