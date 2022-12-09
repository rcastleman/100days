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

# def outer_function():
#     print("I am Outer")

#     def nested_function():
#         print("I am Inner")
    
#     nested_function()

# outer_function()

#return a function from another function

def outer_function():
    print("I am Outer")

    def nested_function():
        print("I am Inner")
    
    return nested_function

inner_function = outer_function()
inner_function()

