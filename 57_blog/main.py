from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/1e222d179ee8b4e58a05'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html",post = all_posts)

if __name__ == "__main__":
    app.run(debug=True)
