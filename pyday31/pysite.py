from flask import Flask

app = Flask(__name__)

@app.route()
def homepage():
    return  "eu te amo meu amor S2"

app.run()
