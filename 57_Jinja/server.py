from flask import Flask,render_template
import random
import datetime
year = datetime.date.today().year

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html",num=random_number,year=year)
 
if __name__ == "__main__":
    app.run(debug=True)
