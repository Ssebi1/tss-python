import unittest
from app.ReservationSystemMutant2 import ReservationSystemMutant2
from utils.exceptions import ReservationNotFoundException


class ReservationDeleteTestCase(unittest.TestCase):

    def setUp(self):
        self.reservation_system = ReservationSystemMutant2()

    def test_delete_reservation(self):
        response = self.reservation_system.add_reservation(**{"name": "Sebi", "check_in": "2021-01-01", "check_out": "2021-01-03", "room_number": 1, "guests": 2})
        reservation_id = 1
        response = self.reservation_system.delete_reservation(reservation_id)
        self.assertEqual(response["status"], "success")

    def test_delete_reservation_not_found(self):
        with self.assertRaises(ReservationNotFoundException):
            self.reservation_system.delete_reservation(999)
