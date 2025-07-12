import os
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
)
def find_highest_bidder(bidding_record):
    """Find the person with the 
    highest bid among all participants"""
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid= bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")      
    
print("Welcome to the Blind Auction")
bid = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name? : ")
    price = int(input("What is your bid? : $"))
    bid[name]=price
    should_continue = input("Are there any other bidder? Type 'yes' or 'no' :  ").lower()
    if should_continue=="no":
        bidding_finished = True
        find_highest_bidder(bid)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')


