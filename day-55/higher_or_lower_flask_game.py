from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0,9)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

@app.route('/')
@make_bold
def home():
    return '<h1>Guess the Number between 0 and 9</h1>' \
           '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:guess>')
def guess_number(guess):
    
    if guess < random_number:
        return '<h1>Too low, Try again!!</h1>' \
               '<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > random_number:
        return '<h1>Too High, Try again!!</h1>' \
               '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"'
    else:
        return '<h1>You Found Me!!</h1>' \
               '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
