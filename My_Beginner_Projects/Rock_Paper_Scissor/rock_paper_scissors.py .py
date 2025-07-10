import random 
print("Welcome to my Rock , Paper , Scissors Game")
a = input("Enter your choice (rock,paper or scissor) : ").lower()
game = random.randint(0,2)
if game== 0:
    x = "rock"
    print("Opponent choose rock")
elif game==1:
     x= "paper"  
     print("Opponent choose paper")
else:
     x= "scissor"
     print("Opponent choose scissor")
     
if a=="rock" and x=="rock":
     print(" Draw")    
elif a=="rock" and x=="scissor":
    print("You Win")
elif a=="rock" and x=="paper":
    print ("You Lose")
elif a=="paper" and x=="rock":
    print("You Win")
elif a=="paper" and x== "paper":
    print("Draw")
elif a=="paper" and x=="scissor":
    print ("You Lose")
elif a=="scissor" and x=="rock":
    print ("You Lose")
elif a=="scissor" and x=="paper":
    print("You Win")
elif a=="scissor" and x=="scissor":
    print("Draw")
else:
    print ("Invalid Input")