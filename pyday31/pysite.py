from flask import Flask

app = Flask(__name__)

@app.route("/teamo")
def homepage():
    return  "eu te amo meu amor S2"

app.run(debug = True)
