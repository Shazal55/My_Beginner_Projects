import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/           ''')
stages = [''' _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      | |
     |
    _|___''',''' _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___''',''' _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___''',''' _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___''',''' _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___''',''' _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___''',''' _______
     |/      
     |      
     |      
     |       
     |      
     |
    _|___''']
word_list = [
    'puzzle', 'rocket', 'jungle', 'castle', 'pirate',
    'planet', 'wizard', 'candle', 'basket', 'velvet',
    'button', 'secret', 'oxygen', 'silver', 'magnet',
    'helmet', 'cactus', 'throne', 'marble', 'dragon',
    'ticket', 'forest', 'bubble', 'hammer', 'crayon',
    'laptop', 'camera', 'drawer', 'guitar', 'window'
]

chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
lives = 6
display = []
for _ in range(word_length) :
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f"You have already entered {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if(letter == guess):
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.\n You loose a life❤")
        lives-=1
        if lives==0:
            end_of_game = True
            print("------YOU LOSE------")
            print(f"The word was \"{chosen_word}\"")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("------YOU WIN------")
    print(stages[lives])
