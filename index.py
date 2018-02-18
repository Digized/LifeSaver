#!/usr/bin/env python3
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/phone")
def phone():
    return render_template("app.html", name="Zuraiz")