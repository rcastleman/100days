from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        print(f"<b> {func()} </b>")


@app.route('/')
def hello_world():
    return '<h2 style = "text-align: center"> Hello, World!</h2>'\
        '<p>This is a new paragraph.</p>'\
        '<img src = "https://media.giphy.com/media/hSoFXPq2J3PWvYKyUn/giphy.gif" width=400>'

@app.route('/bye')
@app.make_bold
# @app.make_emphasis
# @app.make_underline
def say_bye():
    return 'bye'

# @app.route("/username/<path:name>")
# @app.route("/username/<name>")
@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f'Hello {name}, you are {number} years old but you only look {number-30}!'

if __name__ == "__main__":
    app.run(debug=True)
