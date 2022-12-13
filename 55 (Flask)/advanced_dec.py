# from flask import Flask

class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False
    

def create_blog(user):
    print(f"This is {user.name}'s blog post")

def is_authenticated_decorator(function):
    def wrapper():
        if user.is_loggedin = True:
            function()
    return wrapper

Randy = User('Randy')

create_blog(Randy)
