import unittest
from app.ReservationSystem import ReservationSystem
from app.ReservationSystemMutant1 import ReservationSystemMutant1
from app.ReservationSystemMutant2 import ReservationSystemMutant2
from utils.exceptions import InvalidCheckOutDate, InvalidNumberOfGuests, RoomAlreadyBookedException
from utils.datagenerator import test_data


class ReservationEPTestCase(unittest.TestCase):

    def setUp(self):
        self.reservation_system = ReservationSystemMutant2()
        self.test_data = test_data["ep"]

    def test_valid_reservation(self):
        response = self.reservation_system.add_reservation(**self.test_data["valid"])
        self.assertEqual(response["status"], "success")

    def test_invalid_checkout_date(self):
        with self.assertRaises(InvalidCheckOutDate):
            self.reservation_system.add_reservation(**self.test_data["wrong_check_in"])

    def test_invalid_guests(self):
        with self.assertRaises(InvalidNumberOfGuests):
            self.reservation_system.add_reservation(**self.test_data["wrong_guests"])

    def test_room_already_booked(self):
        self.reservation_system.add_reservation(**self.test_data["valid"])
        with self.assertRaises(RoomAlreadyBookedException):
            self.reservation_system.add_reservation(**self.test_data["room_occupied"])

