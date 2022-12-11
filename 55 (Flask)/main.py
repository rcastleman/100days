from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'bye'

# @app.route("/username/<path:name>")
# @app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f'Hello {name}, you are #{number}!'

if __name__ == "__main__":
    app.run(debug=True)
