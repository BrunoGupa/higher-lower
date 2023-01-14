from flask import Flask
import random

# First export the environment variable:
# Open terminal: export FLASK_APP=server.py

app = Flask(__name__)


@app.route("/")
def instructions():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media2.giphy.com/media/3ov9k9AyzTiUCfsZrO/giphy.webp?cid=ecf05e47l6s30tmptdihfmak5b7f87h7gpnx71hm91amvmn5&rid=giphy.webp&ct=g' width=400>" \
           "<p>Write in the addres of the server bar '/number' where number is the number you choose."


magic_number = random.randint(0, 9)


@app.route("/<int:number>")
def detect_user_name(number):
    if number == magic_number:
        return "<h1 style='color:green;'>You found me</h1>" \
               "<img src='https://media0.giphy.com/media/Puc4FZWExJc0E/200.webp?cid=ecf05e47f8leq8t83w7jsoq8smtyrp5mat6l4i1jbyvb4zmr&rid=200.webp&ct=g' width=400>"
    elif number < magic_number:
        return "<h1 style='color:red;'>Too low, try again!</h1>" \
               "<img src='https://media3.giphy.com/media/tsIFjie7obBM4/200w.webp?cid=ecf05e47akaq9y290b4b4393aam2177k8sgqd3rz86zei68x&rid=200w.webp&ct=g' width=400>"
    else:
        return "<h1 style='color:blue;'>Too high, try again!</h1>" \
               "<img src='https://media4.giphy.com/media/3o6ZtaO9BZHcOjmErm/200.webp?cid=ecf05e47onngq29jn90f4i19c9dbojeq1zoozzwpna17fq3v&rid=200.webp&ct=g' width=400>"


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
