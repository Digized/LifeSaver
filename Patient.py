class Patient:
    def __init__(self, healthCardId, firstName,lastName, dateOfBirth, sex, phoneNumber, primaryAddress, healthCondition):
        self.healthCardId=healthCardId
        self.firstName=firstName
        self.lastName=lastName
        self.dateOfBirth=dateOfBirth
        self.sex=sex
        self.phoneNumber=phoneNumber
        self.address=address
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
        return "gps coordinates"

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
