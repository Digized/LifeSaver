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
        self.create_booking()

    def get_end_time(self):
        return self.endTime
        # return self.endTime
    def set_end_time(self,time):
        self.endTime=time

    def set_start_time(self,time):
        self.startTime=time
    def get_start_time(self):
        return self.startTime
    def getPatient(self):
        return self.patient
    def get_short_description(self):
        return self.shortDescription
    def get_queue_number(self):
        return self.queueNumber
    def get_emergency_level(self,healthCardNum):
        return seld.emergancylevel
    def get_booking_state(self,healthCardNum):
        return self.bookingState
    def get_patient_location(self,healthCardNum):
        return self.patientLocation
    def get_notes(self,healthCardNum):
        return self.notes
    def set_queue_number(self,newQueueNumber):
        self.queueNumber=newQueueNumber
    def set_notes(self,newNotes):
        self.notes=newQueueNumber
    def set_booking_state(self,newState):
        self.bookingState=newState
    def set_emergency_level(self,newEmergencyLevel):
        self.emergancylevel=newEmergencyLevel
    def set_description(self,newDescription):
        self.shortDescription=newDescription
    def set_patient_location(self,newLocation):
        self.patientLocation=newLocation
    def set_patient(self,newPatient):
        self.patient=newPatient
    # def create_booking(self):
    #     client=MongoClient()
    #     db=client.booking_object_database
    #     collection=db.booking_object_collection
    #     bookings=db.bookings
    #     booking_data={
    #         'healthCardId':self.patient.healthCardId,
    #         'description':self.shortDescription,
    #         'queueNumber':self.queueNumber,
    #         'emergencyLevel':self.emergencyLevel,
    #         'patientLocation': self.patientLocation,
    #         'notes':self.notes,
    #         'bookingState':self.bookingState,
    #         'startTime':self.startTime,
    #         'endTime':self.endTime
    #     }
    #     result=bookings.insert_one(booking_data)
    def toJSON(self):
        val = {
            'healthCardId':self.patient.healthCardId,
            'description':self.shortDescription,
            'queueNumber':self.queueNumber,
            'emergencyLevel':self.emergencyLevel,
            'patientLocation': self.patientLocation,
            'notes':self.notes,
            'bookingState':self.bookingState,
            'startTime':self.startTime,
            'endTime':self.endTime
        }
        return val
    def updatetoJSON(self,id):
        val={'healthCardId':self.patient.healthCardId},
        {
            '$set':{
                'description':self.shortDescription,
                'queueNumber':self.queueNumber,
                'emergencyLevel':self.emergencyLevel,
                'patientLocation': self.patientLocation,
                'notes':self.notes,
                'bookingState':self.bookingState,
                'startTime':self.startTime,
                'endTime':self.endTime
            }
        }
        return val
    @staticmethod
    def create(patient):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        result=bookings.insert(booking.toJSON())
        return patient.get_healthCardId();
    @staticmethod
    def getBookingByHC(healthcardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        result=bookings.find({'healthCardId':healthCardNum})
        return result
    @staticmethod
    def updateBooking(id,booking):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        result=bookings.update(booking.updatetoJSON(id))
        return booking.getPatient().get_healthCardId();
