def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculate(calculation,n1,n2):
    return calculation(n1,n2)

result = calculate(add,2,3)

print(result)
