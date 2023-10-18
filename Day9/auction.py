from auction_art import logo

print(logo)


bidders_list = []
is_bidding = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of £{highest_bid}")


bidder = {}
while is_bidding:
    user = input("What is your name: ")
    bidding_price = int(input("How much are you bidding? : £"))

    bidder[user] = bidding_price

    more_bidders = input('Are there any more bidders? "yes" or "no" : ')
    if more_bidders == "no":
        find_highest_bidder(bidder)
        is_bidding = False
