import datetime
from pymongo import *
class BookingObject:
    def __init__(self,patient,shortDescription,emergencyLevel):
        self.patient=patient
        self.shortDescription=shortDescription
        self.queueNumber=0
        self.emergencyLevel=emergencyLevel
        self.patientLocation=patient.get_current_location()
        self.notes=""
        self.bookingState='waiting'
        self.startTime=datetime.datetime.now()
        self.endTime=datetime.datetime.now()
        client=MongoClient()
        db=client.booking_object
        # self.create_database()
    def get_end_time(self):
        self.endTime= datetime.datetime.now()
        return self.endTime
    def get_patient(self):
        return self.patient
    def get_start_time(self):
        return self.startTime
    def get_short_description(self):
        return self.shortDescription
    def get_queue_number(self):
        return self.queueNumber
    def get_emergency_level(self):
        return self.emergencyLevel
    def get_booking_state(self):
        return bookingState
    def get_patient_location(self):
        return self.patientLocation
    def get_notes(self):
        return self.notes
    def set_queue_number(self,queueNumber):
        self.queueNumber=queueNumber
    def set_notes(self,notes):
        self.notes=notes
    def set_booking_state(self,state):
        self.bookingState=state
    def create_database(self):
        patient_i=patient_info(self.patient.firstName,self.patient.lastName,self.patient.healthCardId,self.patient.dateOfBirth,
        self.patient.sex,self.patient.phoneNumber,self.patient.primaryAddress,self.patient.healthCondition).save()
        booking=booking_object(patient_i,self.shortDescription,self.patientLocation,self.queueNumber,self.emergencyLevel,
        self.notes,self.bookingState,self.startTime,self.endTime)
        booking.save()
    def getDatabase(self):
        for book in booking_object.objects:
            print(book.description)
            print(book.patient_information.health_card_id)
    def deleteDatabases(self):
        for book in booking_object.objects:
            book.delete()
    def editBookingInfoDatabase(self,healthCard,descript,queueNum,patientLoc,emergencyLvl,notes,booking_state):
        for info in booking_object.objects(info.patient_information.health_card_id=healthCard):
                info.update_one(set__queue_number=int(queueNum))
                info.update_one(set__location=patientLoc)
                info.update_one(set__emergency_level=int(emergencyLvl))
                info.update_one(set__notes=str(notes))
                info.update_one(set__booking_state=str(booking_state))
                info.update_one(set__description=str(descript))
                print('success')
class patient_info(Document):
    first_name=StringField()
    last_name=StringField()
    health_card_id=StringField()
    date_of_birth=StringField()
    sex=StringField()
    phoneNumber=StringField()
    primary_address=StringField()
    health_condition=StringField()
class booking_object(Document):
    patient_information=ReferenceField(patient_info)
    description=StringField()
    location=GeoPointField()
    queue_number=IntField()
    emergency_level=IntField()
    notes=StringField()
    booking_state=StringField()
    start_time=DateTimeField()
    end_time=DateTimeField()
