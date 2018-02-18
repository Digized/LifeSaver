#!/usr/bin/env python3
from Patient import Patient
from BookingObject import BookingObject
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
a = Patient('123444444','232323','Dan Siddiqui','dob','sex','32323232','45mann','helth')
print(a)

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
    return patientcreated

@app.route('/api/user/creatbooking', methods = ["POST"])
def createBooking():
    shortDescription = request.form['shortDescription']
    emergancylevel = request.form['level']
    booking = BookingObject(patient,shortDescription,emergencyLevel)
