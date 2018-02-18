<<<<<<< HEAD
import Patient from Patient
import BookingObject from BookingObject
import operator
#queue is implemented here for each hospital

patientdict = []

 def add_Booking(BookingObject):
     patientdict.append(BookingObject)
     patientdict.sort(key=operator.attrgetter("emergancylevel"), reverse=False)

def delete_Booking(BookingObject):
    patientdict.remove(BookingObject)
    patientdict.sort(key=operator.attrgetter("emergancylevel"), reverse=False)
def sort():
    patientdict.sort(key=operator.attrgetter("emergancylevel"), reverse=False)
def get_list():
    return patientdict
=======
from Patient import Patient
from BookingObject import BookingObject
import operator
#queue is implemented here for each hospital
class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.waitTime = 0
        self.numberofPatients = len(patientdict)
        self.busylevel = ""
        self.patientdict = []

    def add_Booking(BookingObject):
        patientdict.append(BookingObject)
        patientdict.sort(key=operator.attrgetter("emergancylevel"), reverse=False)

    def delete_Booking(BookingObject):
        patientdict.remove(BookingObject)
        patientdict.sort(key=operator.attrgetter("emergancylevel"), reverse=False)
    def sort():
        patientdict.sort(key=operator.attrgetter("emergancylevel"), reverse=False)

    def get_list():
        return patientdict
    def get_number_of_patients():
        return numberofPatients

    def get_wait_time(self):
        hours = ((numberofPatients*20)//60)
        waitTime = hours+":"+((numberofPatients*20)%60)+ "minutes"
        return (waitTime)

    def get_busy_level():
        if numberofPatients >= 20:
            return "high traffic"
        elif numberofPatients >= 7:
            return "medium traffic"
        else:
            return "low traffic"
>>>>>>> master
