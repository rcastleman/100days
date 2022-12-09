import time

def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function


def say_hello():
    time.sleep(2)
    print("Hello")
