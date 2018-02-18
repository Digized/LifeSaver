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
        # self.create_database()
    @staticmethod
    def get_end_time(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'endTime':1,'_id':0})
        if(res==None):
            return -1
        return res['endTime']
        # return self.endTime
    @staticmethod
    def set_end_time(healthCardNum,time):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.update_one({'healthCardId':healthCardNum},{'$set':{'endTime':time}})
        endTime=time
    @staticmethod
    def get_start_time(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'startTime':1,'_id':0})
        if(res==None):
            return -1
        return res['startTime']
    
    @staticmethod
    def get_short_description(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'description':1,'_id':0})
        if(res==None):
            return -1
        return res['description']
    @staticmethod
    def get_queue_number(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'queueNumber':1,'_id':0})
        if(res==None):
            return -1
        return res['queueNumber']
    @staticmethod
    def get_emergency_level(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'emergencyLevel':1,'_id':0})
        if(res==None):
            return -1
        return res['emergencyLevel']
    @staticmethod
    def get_booking_state(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'bookingState':1,'_id':0})
        if(res==None):
            return -1
        return res['bookingState']
    @staticmethod
    def get_patient_location(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'patientLocation':1,'_id':0})
        if(res==None):
            return -1
        return res['patientLocation']
    @staticmethod
    def get_notes(healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        res=bookings.find_one({'healthCardId':healthCardNum},{'notes':1,'_id':0})
        if(res==None):
            return -1
        return res['notes']
    def set_queue_number(self,queueNumber):
        self.queueNumber=queueNumber
    def set_notes(self,notes):
        self.notes=notes
    def set_booking_state(self,state):
        self.bookingState=state

    def create_database(self):
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
        print('One post: {0}'.format(result.inserted_id))
    def getDatabase(self):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        for booking in bookings.find():
            print(booking)
        return bookings
    def updatePatientName(self,healthCardNum,newName):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'name':newName
            }
        }
        )
        # //print(result.matched_count)
    def updatePatientDOB(self,healthCardNum,newDOB):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'dateOfBirth':newDOB
            }
        }
        )
    def updatePatientPhoneNumber(self,healthCardNum,newPhoneNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'phoneNumber':newPhoneNum
            }
        }
        )
    def updatePatientAddress(self,healthCardNum,newAddress):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'name':newName
            }
        }
        )
    def updatePatientHealthCondition(self,healthCardNum,newhealthCondition):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'healthCondition':newhealthCondition
            }
        }
        )
    def updateDescription(self,healthCardNum,newDescription):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'description':newDescription
            }
        }
        )
    def updatequeueNum(self,healthCardNum,newQueueNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'queueNumber':newQueueNum
            }
        }
        )
    def updateEmergencyLevel(self,healthCardNum,newEmergencyLevel):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'emergencyLevel':newEmergencyLevel
            }
        }
        )
    def updatePatientLocation(self,healthCardNum,newLocation):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'patientLocation':newLocation
            }
        }
        )
    def updateNotes(self,healthCardNum,newNotes):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'notes':newNotes
            }
        }
        )
    def updateBookingState(self,healthCardNum,newBookingState):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'bookingState':newBookingState
            }
        }
        )
    def updateEndTime(self,healthCardNum,newEndTime):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'endTime':newEndTime
            }
        }
        )
    def updatePatientSex(self,healthCardNum,newSex):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.update(
        {'healthCardId':healthCardNum},
        {
            '$set': {
                'sex':newSex
            }
        }
        )
    def deleteDocument(self,healthCardNum):
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        result=db.bookings.delete_many({'healthCardId':healthCardNum})
    def deleteDatabases(self):
         client=MongoClient()
         db=client.booking_object_database
         collection=db.booking_object_collection
         db.bookings.drop()
    #     for book in booking_object.objects:
    #         book.delete()
    # def editBookingInfoDatabase(self,healthCard,descript,queueNum,patientLoc,emergencyLvl,notes,booking_state):
    #     for info in booking_object.objects(info.patient_information.health_card_id=healthCard):
    #             info.update_one(set__queue_number=int(queueNum))
    #             info.update_one(set__location=patientLoc)
    #             info.update_one(set__emergency_level=int(emergencyLvl))
    #             info.update_one(set__notes=str(notes))
    #             info.update_one(set__booking_state=str(booking_state))
    #             info.update_one(set__description=str(descript))
    #             print('success')
