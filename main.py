from flask import Flask
import random

app = Flask(__name__)
random_number=random.randint(0,9)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnBlM2ZwYXU1aWJ2bGJ4Z3VrNWtkcmNicG9ibHN5Nmk4azJiN3pzcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:num>")
def check(num):
    if num>random_number:
        return "<h1>Too high, try again...</h1>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    elif num<random_number:
        return "<h1>Too low, try again...</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    else :
        return "<h1>You Found Me!!!</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"



if __name__=="__main__":
    app.run(debug=True)