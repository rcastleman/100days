from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'bye'

if __name__ == "__main__":
    app.run()

    def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function