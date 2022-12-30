from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

blog_url = 'https://api.npoint.io/1e222d179ee8b4e58a05'
response = requests.get(blog_url)
# all_posts = response.json()
all_post = "static/blog_text.txt"

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/post/<int:index>")
def show_post(index):
    for blog_post in all_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html",post = requested_post)
