from flask import Flask

app = Flask(__name__)

def make_bold(function)
    def wrapper():
        return '<b>' +  function() + '</b>'
    return wrapper


@app.route('/')
def hello_world():
    return '<h2 style = "text-align: center"> Hello, World!</h2>'\
        '<p>This is a new paragraph.</p>'\
        '<img src = "https://media.giphy.com/media/hSoFXPq2J3PWvYKyUn/giphy.gif" width=400>'

@make_bold()
@app.route('/bye')
def say_bye():
    return 'bye'

# @app.route("/username/<path:name>")
# @app.route("/username/<name>")
@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f'Hello {name}, you are {number} years old but you only look {number-30}!'

if __name__ == "__main__":
    app.run(debug=True)
