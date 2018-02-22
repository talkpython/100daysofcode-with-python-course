#!python3

from flask import Flask, render_template
from data import fave_beer

app = Flask(__name__)

@app.route("/")
def index():   
    return render_template("index.html",
                           fave_beer=fave_beer)

if __name__ == "__main__":
    app.run()
