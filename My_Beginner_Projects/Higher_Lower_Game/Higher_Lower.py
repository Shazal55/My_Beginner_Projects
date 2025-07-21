import random
import os
from data import data
print("""                                              
|  \  |  \|  \          |  \                                
| $$  | $$ \$$  ______  | $$____    ______    ______        
| $$__| $$|  \ /      \ | $$    \  /      \  /      \       
| $$    $$| $$|  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\      
| $$$$$$$$| $$| $$  | $$| $$  | $$| $$    $$| $$   \$$      
| $$  | $$| $$| $$__| $$| $$  | $$| $$$$$$$$| $$            
| $$  | $$| $$ \$$    $$| $$  | $$ \$$     \| $$            
 \$$   \$$ \$$ _\$$$$$$$ \$$   \$$  \$$$$$$$ \$$            
              |  \__| $$                                    
               \$$    $$                                    
                \$$$$$$                                     
             __                                             
            |  \                                            
            | $$  ______   __   __   __   ______    ______  
            | $$ /      \ |  \ |  \ |  \ /      \  /      \ 
            | $$|  $$$$$$\| $$ | $$ | $$|  $$$$$$\|  $$$$$$|
            | $$| $$  | $$| $$ | $$ | $$| $$    $$| $$   \$$
            | $$| $$__/ $$| $$_/ $$_/ $$| $$$$$$$$| $$      
            | $$ \$$    $$ \$$   $$   $$ \$$     \| $$      
             \$$  \$$$$$$   \$$$$$\$$$$   \$$$$$$$ \$$      
                                                            
                                                            
                                                            """)

def format_data(account):
    name = account["name"]
    lang = account["language"]
    continent = account["continent"]
    return f"{name}, where the official language is {lang}, located in {continent}."

def check_answer(guess, a_pop, b_pop):
    if a_pop > b_pop:
        return guess == "a"
    else:
        return guess == "b"

score = 0
account_b = random.choice(data)
game_should_continue = True

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("""
    ____   ____     
    \   \ /   /_____
     \   Y   /  ___/
      \     /\___ \ 
       \___//____  >
                   
    """)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Which country has a higher population? Type 'A' or 'B': ").lower()
    a_pop = account_a["population (millions)"]
    b_pop = account_b["population (millions)"]

    is_correct = check_answer(guess, a_pop, b_pop)
    os.system('cls' if os.name == 'nt' else 'clear')

    if is_correct:
        score += 1
        print(f"You're right! 🎉 Current score: {score}\n")
    else:
        print(f"You're wrong 😒. Final score: {score}")
        game_should_continue = False