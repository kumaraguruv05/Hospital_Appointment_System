from hospital import book_appointment

def test_booking():
    assert book_appointment("John","Smith") == "Appointment booked for John with Dr.Smith"
