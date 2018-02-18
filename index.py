#!/usr/bin/env python3
import os
from Patient import Patient
from BookingObject import BookingObject
from io import open
from flask import Flask, render_template, jsonify, request, redirect
from werkzeug.utils import secure_filename
from google.cloud import vision
from google.cloud.vision import types
from Hospital import Hospital
import operator

UPLOAD_FOLDER = os.path.dirname(__file__)+'/tmpfiles/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

hospital1 = Hospital("Ottawa Hostpital", "123 Hospital.Rd",ho1)

hospital2 = hospital2("City Clinic,", "66 Town.st",ho2)

listOfHospital = [hospital1, hospital2]
def lbh(listOfHospital):
    listOfHospital.sort(key=operator.attrgetter("numberofPatients"), reverse=False)
    return list[0]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/clinic/")
def deletdashboard():
    return render_template("dashboard.html", data=data)

@app.route("/clinic/<name>/")
def dashboard(name):
    return render_template("dashboard.html", data=data)

@app.route("/user/<id>")
def getuser(id):
    patient = Patient.find_by_HC(id)
    return render_template("user.html", patient=patient)

@app.route("/user/", methods=["POST"])
@app.route("/user/create",methods = ["GET"])
@app.route("/user/<id>/edit", methods=["POST","GET"])
def modifyuser(id=None):
    if(request.method=="POST"):
        if(id):
            Patient.update(id, create_patient(request.form))
        else:
            id = Patient.create(create_patient(request.form))
        newUrl = "/user/" + id
        return redirect(newUrl)
    if(request.method=="GET"):
        patient = Patient.find_by_HC(id)
        return render_template("edituser.html", patient=patient)

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

def create_patient(form):
    name = form['name']
    healthCardId = form['healthCardId']
    dateOfBirth = form['dateOfBirth']
    sex = form['sex']
    expiryDate = form['expiryDate']
    primaryAddress = form['primaryAddress']
    phoneNumber = form['phoneNumber']
    healthCondition = form['healthCondition']
    patientcreated = Patient(healthCardId, expiryDate, name, dateOfBirth, sex, phoneNumber, primaryAddress, healthCondition)
    return patientcreated

@app.route('/api/user/creatbooking', methods = ["POST"])
def createBooking():
    shortDescription = request.form['shortDescription']
    emergancylevel = request.form['level']
    patient = request.form['Patient']
    booking = BookingObject(patient,shortDescription,emergencyLevel)
