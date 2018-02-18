#!/usr/bin/env python3
import os
from Patient import Patient
from BookingObject import BookingObject
from io import open
from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
from google.cloud import vision
from google.cloud.vision import types


UPLOAD_FOLDER = os.path.dirname(__file__)+'/tmpfiles/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dashboard")
def dashboard():
    data = []
    data.append(Patient('123444444','Dan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('1234444asda44','Dasjdhasksan', 'siddiqui','dob','sex','32323232','45mann','helth'))
    data.append(Patient('12344asdsa4444','Dasdbaskhan', 'siddiqui','dob','sex','32asdas323232','45mann','helth'))
    return render_template("dashboard.html", data=data)

@app.route("/phone")
def phone():
    return render_template("app.html", name="Zuraiz")

@app.route("/user")
def user():
    return render_template("edituser.html", name="Zuraiz")

  @app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_loc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_loc)
            return jsonify(recognize(file_loc))
    return

def recognize(file):
    with open(file, "rb") as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    client = vision.ImageAnnotatorClient()
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels


@app.route('/api/user',methods = ["POST"])
def show_user_profile():
    print ('hello')
    return None

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
    patient = request.form['Patient']
    booking = BookingObject(patient,shortDescription,emergencyLevel)
