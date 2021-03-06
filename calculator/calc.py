import os

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/':divide,
    }

# create string of operations choices
op_choice = ""
for op in operations:
    op_choice += op + " "

def calculator():
    num1 = float(input("What is the first number?: "))

    should_continue = True

    while should_continue:
        
        op = input(f"Which operation ({op_choice}?")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[op]
        answer = calculation_function(num1,num2)
        print(f"{num1} {op} {num2} = {answer} ")
        if input(f"Type 'y' to continue calculation with {answer}: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()