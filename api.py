import flask
from flask import request, jsonify
from random_word import RandomWords

r = RandomWords()

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return """<h1 style="text-align: center;">Welcome to my brilliant website</h1>
    <body style="text-align: center;">Make a request to /word to get a random word</body>"""

@app.route("/word", methods=["GET"])
def GetWord():
    w = r.get_random_word()
    return w


app.run(host="0.0.0.0:PORT80")
