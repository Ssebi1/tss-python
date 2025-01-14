class InvalidCheckOutDate(Exception):
    def __init__(self):
        super().__init__("Check-out date must be after check-in date.")

class InvalidNumberOfGuests(Exception):
    def __init__(self):
        super().__init__("Number of guests must be at least 1.")

class RoomAlreadyBookedException(Exception):
    def __init__(self):
        super().__init__("Room is already booked for the selected dates.")

def ReservationNotFoundException(Exception):
    def __init__(self):
        super().__init__("Reservation not found.")