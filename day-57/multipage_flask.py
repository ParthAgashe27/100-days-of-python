from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests 

now = datetime.today()
app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(1,10)
    year = now.year
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def prediction(name):
    params = {
    "name": name
    }
    AGIFY_ENDPOINT = "https://api.agify.io"
    GENDERIZE_ENDPOINT = "https://api.genderize.io"

    age_response = requests.get(AGIFY_ENDPOINT, params=params).json()
    gender_response = requests.get(GENDERIZE_ENDPOINT, params=params).json()
    return render_template('guess.html', gender=gender_response['gender'], age=age_response['age'], name=name)

@app.route('/blog')
def get_blog():
    BLOG_URL = "https://api.npoint.io/58d3a06889af64384365"
    blog_response = requests.get(BLOG_URL)
    all_posts = blog_response.json()
    return render_template('blog.html' ,posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

