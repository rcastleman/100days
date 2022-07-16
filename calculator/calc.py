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

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
op = input(f"Which operation ({op_choice}?")

calculation_function = operations[op]
answer = calculation_function(num1,num2)

# answer = operations["op_choice"]
print(f"{num1} {op} {num2} = {answer} ")
