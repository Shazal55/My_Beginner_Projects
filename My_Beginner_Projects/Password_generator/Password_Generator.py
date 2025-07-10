import random
letters = ['A','B','C','D','E','F','G','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','10']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','=','_','+']
print("Welcome to the Password Generator")
nr_letters = int(input(f"How many letters you want in your password : \n"))
nr_numbers = int(input(f"How many numbers you want in your password : \n"))
nr_symbols = int(input(f"How many symbols you want in your password : \n"))
password_list = []
for char in range (1,nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))
for char in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = "" 
for char in password_list:
    password +=char
print(f"your final password is : {password}")




