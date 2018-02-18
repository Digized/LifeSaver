#!/usr/bin/env python3
import Patient from Patient
import BookingObject from BookingObject
from flask import Flask, render_template, request, jsonify
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

@app.route('/api/user',methods = ["POST"])
def create_patient():
    name = request.form['name']
    healthCardId = request.form['healthCardId']
    dateOfBirth = request.form['dateOfBirth']
    sex = request.form['sex']
    expiryDate = request.form['expiryDate']
    primaryAddress = request.form['primaryAddress']
    phoneNumber = request.form['phoneNumber']
    healthCondition = request.form['healthCondition']


    patientcreated = Patient(healthCardId, expiryDate, name, dateOfBirth, sex, phoneNumber, primaryAddress, healthCondition)
    patientlist.add(patientcreated)
    return patientcreated
patientlist []
def create_Booking(patientcreated):



# a = patient()
# try:
#     import Queue as Q  # ver. < 3.0
# except ImportError:
#     import queue as Q
#
# q = Q.PriorityQueue()
# q.put((Booking.get_emergency_level(),Booking Obj))
# q.put((1,'one'))
# q.put((5,'five'))
# while not q.empty():
#     print q.get(),
