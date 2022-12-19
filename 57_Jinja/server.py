from flask import Flask,render_template
import random
import datetime
import requests


app = Flask(__name__)

year = datetime.date.today().year

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html",num=random_number,year=year)

#------ Name Route--------#
URL = 'https://api.agify.io?name='


@app.route('/guess/<input_name>')
def guess_name(input_name):
    response = requests.get(URL+input_name)
    data = response.json()
    age = data['age']
    return render_template('name.html',name=input_name.title(),age=age)
 
if __name__ == "__main__":
    app.run(debug=True)
