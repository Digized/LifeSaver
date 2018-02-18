import requests
import json
from pymongo import *


class Patient:
    def __init__(self, healthCardId,expiryDate, name, dateOfBirth, sex, phoneNumber, primaryAddress, healthCondition):
        self.healthCardId=healthCardId
        self.expiryDate=expiryDate
        self.name=name
        self.dateOfBirth=dateOfBirth
        self.sex=sex
        self.phoneNumber=phoneNumber
        self.primaryAddress=primaryAddress
        self.healthCondition=healthCondition

    def get_healthCardId(self):
        return self.healthCardId
    def get_expiryDate(self):
        return self.expiryDate
    def get_name(self):
        return self.name
    def get_dateOfBirth(self):
        return self.dateOfBirth
    def get_sex(self):
        return self.sex
    def get_phoneNumber(self):
        return self.phoneNumber
    def get_primaryAddress(self):
        return self.primaryAddress
    def get_current_location(self):
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        city = j['city']
        return "latitude: "+str(lat)+ " longitude: "+ str(lon)

    def get_health_condition(self):
        return self.healthCondition

    def set_name(self, newname):
        self.name = newname
    def set_healthCardId(self, newhealthCardId):
        self.healthCardId = newhealthCardId
    def set_expiryDate(self, newExpiryDate):
        self.expiryDate = newExpiryDate
    def set_dateOfBirth(self, newdateofbirth):
        self.dateOfBirth = newdateofbirth
    def set_sex(self,newSex):
        self.sex = newSex
    def set_phoneNumber(self,newphoneNumber):
        self.phoneNumber = newphoneNumber
    def set_primaryAddress(self, newAddress):
        self.primaryAddress=newAddress
    def set_healthCondition(self, newhealthCondition):
        self.healthCondition = newhealthCondition
    
    def toJSON(self):
        val = {
            "healthCardId": self.healthCardId,
            "expiryDate":self.expiryDate,
            "name":self.firstname,
            "dateOfBirth":self.dateOfBirth,
            "sex":self.sex,
            "phoneNumber":self.phoneNumber,
            "primaryAddress":self.primaryAddress,
            "healthCondition":self.healthCondition        
        }
        return val

    @staticmethod
    def find_by_HC(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.patients
        result=collection.find({'healthCardId':healthCardNum})
        print(result);
    
    @staticmethod
    def create(patient):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.patients
        result=collection.insert(patient.toJSON())
        return patient.get_healthCardId();

# a = Patient('123444444','232323','Dan Siddiqui','dob','sex','32323232','45mann','helth')
# print (a.get_current_location())
