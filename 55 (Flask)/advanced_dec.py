# from flask import Flask

class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog(user):
    print(f"This is {user.name}'s blog post")

Randy = User('Randy')
Randy.is_logged_in = True

create_blog(Randy)
