from art import *

bidders = {}
winner = {}
art = logo

print(art)
auction = True
while auction:
    user_name = input("What is your name?: ")
    user_bid = input("What's your bid?: ")
    bidders[user_name] = user_bid


    #Add the bidder
    for add_bidder in bidders:
        amount_to_bid = bidders[add_bidder]
        winner[add_bidder] = amount_to_bid

    add_bidder = input("Is there other user wants to bid?: ")
    if add_bidder == 'yes':
        auction = True
    else:
        auction = False

#Determines the winner
max = 0
user_won = ''
for user in winner:
    amount = int(winner[user])
    if amount > max:
        max = amount
        user_won = user
        print(f"The winner is {user_won} with the winning price of {max}")
        auction=False


