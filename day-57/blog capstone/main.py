from flask import Flask, render_template
from post import Post
import requests


POSTS_URL = "https://api.npoint.io/13e71e62dcedb0a54414"
posts = requests.get(POSTS_URL).json()
post_contents = []
for post in posts:
    post_cont = Post(id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
    post_contents.append(post_cont)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_contents)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_contents:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
