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

    def get_end_time(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'endTime':1,'_id':0})
        if(res==None):
            return -1
        return res['endTime']
        # return self.endTime
    def set_end_time(self,healthCardNum,time):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'endTime':time}})
        endTime=time

    def set_start_time(self,healthcardNum,time):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'startTime':time}})
        startTime=time
    def get_start_time(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'startTime':1,'_id':0})
        if(res==None):
            return -1
        return res['startTime']

    def get_short_description(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'description':1,'_id':0})
        if(res==None):
            return -1
        return res['description']
    def get_queue_number(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'queueNumber':1,'_id':0})
        if(res==None):
            return -1
        return res['queueNumber']
    def get_emergency_level(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'emergencyLevel':1,'_id':0})
        if(res==None):
            return -1
        return res['emergencyLevel']
    def get_booking_state(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'bookingState':1,'_id':0})
        if(res==None):
            return -1
        return res['bookingState']
    def get_patient_location(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'patientLocation':1,'_id':0})
        if(res==None):
            return -1
        return res['patientLocation']
    def get_notes(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'notes':1,'_id':0})
        if(res==None):
            return -1
        return res['notes']
    def set_queue_number(self,healthCardNum,newQueueNumber):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'queueNumber':newQueueNumber}})
        queueNumber=newQueueNumber
    def set_notes(self,healthcardNum,newNotes):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'notes':newNotes}})
        notes=newNotes
    def set_booking_state(self,healthCardNumnewState):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'bookingState':newState}})
        bookingState=newState
    def set_emergency_level(self,healthCardNumnewEmergencyLevel):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'emergancylevel':newEmergencyLevel}})
        emergancylevel=newEmergencyLevel
    def set_description(self,healthCardNum,newDescription):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'description':newDescription}})
        description=newDescription
    def set_patient_location(self,healthcardNum,newLocation):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'patientLocation':newLocation}})
        patientLocation=newLocation

    def create_booking(self):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        booking_data={
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
        result=bookings.insert_one(booking_data)
    @staticmethod
    def getBookingByHC(healthcardNum):
        client=MongoClient()
        db=client.booking_object_database
        bookings=db.bookings
        result=bookings.find({'healthCardId':healthCardNum})
        return result
