from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('randy.html')


@app.route('/bye')
def say_bye():
    return 'bye'

if __name__ == "__main__":
    app.run(debug=True)