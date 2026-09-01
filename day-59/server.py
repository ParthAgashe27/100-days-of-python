from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route('/post.html')
def get_post():
    return render_template("post.html")

@app.route('/index.html')
def get_index():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")
