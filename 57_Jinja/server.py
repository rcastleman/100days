from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

app.route('/')
def random_function():
    random_number = random.randint(1,10)
    return render_template("index.html",num=random_number)


@app.route('/')
def root():
    return render_template('index.html')
    # return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
