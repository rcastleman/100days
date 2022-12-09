import time

def delay(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay
def say_hello():
    print("Hello")
