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

#------ Age & Gender Route--------#
AGIFY = 'https://api.agify.io?name='
GENDERIZE = 'https://api.genderize.io?name='

@app.route('/guess/<input_name>')
def guess(input_name):
    
    age_response = requests.get(AGIFY+input_name)
    age_data = age_response.json()
    age = age_data['age']

    gender_response = requests.get(GENDERIZE+input_name)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    return render_template('name.html',name=input_name.title(),age=age,gender=gender)
 
if __name__ == "__main__":
    app.run(debug=True)
