#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hello World!"
=======
    return render_template('index.html')
>>>>>>> 9f9dd16ec5fb9ee8abcf6e2437ebb4d978478870
