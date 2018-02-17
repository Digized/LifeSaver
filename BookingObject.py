class BookingObject:
    def __init__(self,patient,shortDescription,emergencyLevel):
        self.patient=patient
        self.shortDescription=shortDescription
        self.queueNumber
        self.emergencyLevel=emergencyLevel
        self.patientLocation=patient.get_location()
        self.notes=""
        self.bookingState='waiting'
    def get_patient(self):
        return self.patient
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
    
