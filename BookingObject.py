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

        self.create_database()
    def get_end_time(self):
        self.endTime= datetime.datetime.now()
        return self.endTime
    def set_end_time(self, time):
        endTime=time
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
        client=MongoClient()
        db=client.booking_object_database
        collection=db.booking_object_collection
        bookings=db.bookings
        booking_data={
            'name': self.patient.firstname,
            'healthCardId': self.patient.healthCardId,
            'expiryDate':self.patient.expiryDate,
            'dateOfBirth':self.patient.dateOfBirth,
            'sex':self.patient.sex,
            'phoneNumber':self.patient.phoneNumber,
            'primaryAddress':self.patient.primaryAddress,
            'healthCondition':self.patient.healthCondition,
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
