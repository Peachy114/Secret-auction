from art import *

art = logo
print(art)
def finding_winner(bidding):
    #Determines the winner
    user_won = ''
    high_bid = 0

    max(bidding)
    for bidder in bidding:
        amount = int(bidding[bidder])
        if amount > high_bid:
            high_bid = amount
            user_won = bidder
    print(f"The winner is {user_won} with the winning price of {high_bid}")


bidders = {}
auction = True
while auction:
    user_name = input("What is your name?: ")
    user_bid = input("What's your bid?: ")
    bidders[user_name] = user_bid

    add_bidder = input("Is there other user wants to bid?: ")
    if add_bidder == 'no':
        auction = False
        finding_winner(bidders)
        print("\n" * 20)
    else:
        auction = True

