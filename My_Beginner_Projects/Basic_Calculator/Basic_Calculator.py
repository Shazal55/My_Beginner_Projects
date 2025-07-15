import os
def calculator():
    print("""    _____________________
            |  _________________  |
            | | JO           0. | |
            | |_________________| |
            |  ___ ___ ___   ___  |
            | | 7 | 8 | 9 | | + | |
            | |___|___|___| |___| |
            | | 4 | 5 | 6 | | - | |
            | |___|___|___| |___| |
            | | 1 | 2 | 3 | | x | |
            | |___|___|___| |___| |
            | | . | 0 | = | | / | |
            | |___|___|___| |___| |
            |_____________________|
""")
#CALCULATOR

    #ADD
    def add(n1,n2):
        return n1 + n2
    #subtract
    def sub(n1,n2):
        return n1 -n2
    #multiply
    def multiply(n1,n2):
        return n1*n2
    #divide
    def divide(n1,n2):
        return n1 / n2
    operations = {"+" : add,
                "-":sub,
                "*":multiply,
                "/":divide
    }
    num1 = float(input("Whats the first number : "))
    for symbol in operations:
            print(symbol)
    to_continue = True
    while to_continue:
        operation_symbol = input("Pick the operation : ")
        num2 = float(input("Whats the next number : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} ={answer}")
        should_stop =  input(f"Type y to continue calculating with {answer} , or type n to start a new calculation or type x to exit : ")
        if should_stop == "n":
            to_continue = False
            calculator()
        elif should_stop == "x":
            to_continue = False
        else:
            num1 = answer

calculator()