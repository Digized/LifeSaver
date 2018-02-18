#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/phone")
def phone():
    return render_template("app.html", name="Zuraiz")

@app.route("/user")
def user():
    return render_template("edituser.html", name="Zuraiz")

@app.route("/uploadImage", methods="POST")
def uploadImage():
    return "nothing for now";

@app.route('/api/user',methods = ['POST'])
def show_user_profile():
    print ('hello')
    return None
# a = patient()
# try:
#     import Queue as Q  # ver. < 3.0
# except ImportError:
#     import queue as Q
#
# q = Q.PriorityQueue()
# q.put((Booking.level(),Booking))
# q.put((1,'one'))
# q.put((5,'five'))
# while not q.empty():
#     print q.get(),
