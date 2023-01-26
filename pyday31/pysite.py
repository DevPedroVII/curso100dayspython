from flask import Flask

app = Flask(__name__)

def homepage():
    return  "eu te amo meu amor S2"

app.run()
