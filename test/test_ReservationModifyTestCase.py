import unittest

from app.ReservationSystemMutant2 import ReservationSystemMutant2
from utils.exceptions import ReservationNotFoundException


class ReservationModifyTestCase(unittest.TestCase):

    def setUp(self):
        self.reservation_system = ReservationSystemMutant2()

    def test_modify_reservation(self):
        self.reservation_system.add_reservation(**{"name": "Sebi", "check_in": "2021-01-01", "check_out": "2021-01-03", "room_number": 1, "guests": 2})
        reservation_id = 1
        response = self.reservation_system.modify_reservation(reservation_id, **{"name": "Sebi2", "check_in": "2021-01-01", "check_out": "2021-01-05", "room_number": 1, "guests": 2})
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["data"]["name"], "Sebi2")
        self.assertEqual(response["data"]["room_number"], 1)
        self.assertEqual(response["data"]["guests"], 2)

    def test_modify_reservation_not_found(self):
        with self.assertRaises(ReservationNotFoundException):
            self.reservation_system.modify_reservation(999, **{"name": "Sebi2", "check_in": "2021-01-01", "check_out": "2021-01-05", "room_number": 1, "guests": 2})
