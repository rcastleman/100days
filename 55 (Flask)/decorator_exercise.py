# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args,**kwargs):
        print(f"You called {function.__name__}{args}\nIt returned: {function(*args)}")
        # print(f"You called {function.__name__}{args}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)

print(a_function(1,2,3,4,5,6,7,8,9))
