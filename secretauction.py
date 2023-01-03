import clear
from auctionart import logo
print(logo)

auction = {}
def details():

    name = input('enter your name:\n')
    value = int(input('enter your bid amount:\n$'))
    auction[name] = value

def highest_bidder(bid_record):
    highest_bid = 0
    winner = ''
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'winner is {winner} with a bid of ${highest_bid}')



again = True
while again:
    details()
    more_user = input('are there more bidders? (type "yes" or "no"):\n')
    if more_user == 'no':
        print('thanks for taking part.The biding is closed')
        again = False
    else:
        clear
highest_bidder(auction)




