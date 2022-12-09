import time

def delay(function):
    def wrapper_function():
        time.sleep(2)
        function()
        time.sleep(2)
    return wrapper_function

# @delay
def say_hello():
    print("Hello")

@delay
def say_bye():
    print("bye")

say_hello()
say_bye()
