import requests
import json

class Patient:
    def __init__(self, healthCardId, firstName,lastName, dateOfBirth, sex, phoneNumber, primaryAddress, healthCondition):
        self.healthCardId=healthCardId
        self.firstName=firstName
        self.lastName=lastName
        self.dateOfBirth=dateOfBirth
        self.sex=sex
        self.phoneNumber=phoneNumber
        self.primaryAddress=primaryAddress
        self.healthCondition=healthCondition

    def get_healthCardId(self):
        return self.healthCardId
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
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
        return "latitude: "+str(lat)+ " longitude: "+ str(city)

    def set_firstName(self, newfirstname):
        self.firstName = newfirstname
    def set_LastName(self, newlastname):
        self.firstName = newlastname
    def set_healthCardId(self, newhealthCardId):
        self.firstName = newhealthCardId
    def set_dateOfBirth(self, newdateofbirth):
        self.dateOfBirth = newdateofbirth
    def set_sex(self,newSex):
        self.sex = newSex
    def set_phoneNumber(self,newphoneNumber):
        self.sex = newphoneNumber
    def set_address(self, newAddress):
        self.primaryAddress=newAddress
    def set_healthCondition(self, newhealthCondition):
        self.healthCondition = newhealthCondition

a = Patient('123444444','Dan', 'siddiqui','dob','sex','32323232','45mann','helth')
print (a.get_current_location())
