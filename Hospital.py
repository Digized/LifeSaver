import Patient from Patient
import BookingObject from BookingObject
import operator
#queue is implemented here for each hospital

patientdict = []

 def add_Booking(BookingObject):
     patientdict.append(BookingObject)
     patientdict.sort()

def delete_Booking(BookingObject):
        patientdict.remove(BookingObject)
        patientdict.sort()
def sort():
    patientdict.sort(key=operator.attrgetter("emergancylevel"), reverse=False)
def get_list():
    return patientdict
