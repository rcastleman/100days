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

result = calculate(multiply,2,3)

# print(result)

#Nested functions

def outer_function():
    print("I am Outer")

    def nested_function():
        print("I'm Inner")
    
    nested_function()

outer_function()
