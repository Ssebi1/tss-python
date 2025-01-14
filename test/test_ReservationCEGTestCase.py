import unittest
from app.ReservationSystem import ReservationSystem
from app.ReservationSystemMutant1 import ReservationSystemMutant1
from app.ReservationSystemMutant2 import ReservationSystemMutant2
from utils.exceptions import InvalidCheckOutDate, InvalidNumberOfGuests, RoomAlreadyBookedException
from utils.datagenerator import test_data


class ReservationCEGTestCase(unittest.TestCase):

    def setUp(self):
        self.reservation_system = ReservationSystemMutant2()
        self.test_data = test_data["ceg"]

    def test_valid_reservation(self):
        for data in self.test_data["valid"]:
            response = self.reservation_system.add_reservation(**data)
            self.assertEqual(response["status"], "success")

    def test_invalid_checkout_date(self):
        for data in self.test_data["wrong_check_in"]:
            with self.assertRaises(InvalidCheckOutDate):
                self.reservation_system.add_reservation(**data)

    def test_invalid_guests(self):
        for data in self.test_data["wrong_guests"]:
            with self.assertRaises(InvalidNumberOfGuests):
                self.reservation_system.add_reservation(**data)

    def test_room_already_booked(self):
        self.reservation_system.add_reservation(**self.test_data["valid"][0])
        for data in self.test_data["room_occupied"]:
            with self.assertRaises(RoomAlreadyBookedException):
                self.reservation_system.add_reservation(**data)

