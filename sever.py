from flask import Flask
import random
random_no = random.choice(range(0, 9))


app = Flask(__name__)

print(__name__)

@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>")

@app.route("/<int:num>")
def guess(num):
    if num == random_no:
        return ("<h1 style='color:green'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>")
    elif num < random_no:
        return ("<h1 style='color:red'>Too low, try again</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>")
    elif num > random_no:
        return ("<h1 style='color:orange'>Too high, try again</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>")

if __name__ == '__main__':
    app.run(debug=True)