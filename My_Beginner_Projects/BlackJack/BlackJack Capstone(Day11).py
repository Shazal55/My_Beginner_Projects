import random
import os
def deal_card():
    """Returns random cards"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """Take a list of cards and return the score calculated from cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    """Compares user score and computer  score"""
    if user_score == computer_score:
        return "It's a DRAW 😒"
    elif computer_score==0:
        return "Lose , Opponent has a BlackJack😱"
    elif user_score == 0:
        return "Win with a BlackJack 😎"
    elif user_score>21:
        return "You went over 21, YOU LOSE 🤦‍♂️"
    elif computer_score>21:
        return "Opponent went over 21, YOU WIN 🤣"
    elif user_score>computer_score:
        return "YOU WIN 😍"
    else:
        return "YOU LOSE 🤷‍♂️"
def play_game():
    print("""------.           _     _            _    _            _    
            |A_  _ |.          | |   | |          | |  (_)          | |   
            |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
            | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
            |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
            `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                |  \/ K|                            _/ |                
                `------'                           |__/                 
""")
    user_card = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_cards)
        print(f" User cards : {user_card} and the user score : {user_score}")
        print(f" computer cards : {computer_cards[0]}")
        if user_score==0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or Type 'n' to pass : ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over=True
    while  computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand :  {user_card} and your final score :  {user_score}")
    print(f"Opponent final  score : {computer_cards} and his final score :{computer_score}")
    print(compare(user_score,computer_score))
while input("Do you want to play the game of BlackJack? Type 'y' or 'n' : ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()