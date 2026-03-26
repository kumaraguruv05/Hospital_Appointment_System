from hospital import book_appointment

def test_booking():
    assert book_appointment("John","Smith") == "Appointment successfully booked for John with Dr.Smith"
