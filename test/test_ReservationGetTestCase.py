import unittest

from app.ReservationSystemMutant2 import ReservationSystemMutant2


class ReservationGetTestCase(unittest.TestCase):

    def setUp(self):
        self.reservation_system = ReservationSystemMutant2()

    def test_get_all_reservations(self):
        response = self.reservation_system.get_all_reservations()
        self.assertEqual(response["status"], "success")
        self.assertEqual(len(response["data"]), 0)

    def test_get_all_reservations_2(self):
        self.reservation_system.add_reservation(**{"name": "Sebi", "check_in": "2021-01-01", "check_out": "2021-01-03", "room_number": 1, "guests": 2})
        response = self.reservation_system.get_all_reservations()
        self.assertEqual(response["status"], "success")
        self.assertEqual(len(response["data"].keys()), 1)
        self.assertEqual(response["data"][1]["name"], "Sebi")
        self.assertEqual(response["data"][1]["room_number"], 1)
        self.assertEqual(response["data"][1]["guests"], 2)

    def test_get_reservation_for_date(self):
        response = self.reservation_system.get_reservations_for_date("2021-02-02")
        self.assertEqual(response["status"], "success")
        self.assertEqual(len(response["data"]), 0)

    def test_get_reservation_for_date_2(self):
        self.reservation_system.add_reservation(**{"name": "Sebi", "check_in": "2021-02-01", "check_out": "2021-02-03", "room_number": 1, "guests": 2})
        response = self.reservation_system.get_reservations_for_date("2021-02-02")
        self.assertEqual(response["status"], "success")
        self.assertEqual(len(response["data"]), 1)
        self.assertEqual(response["data"][0]["name"], "Sebi")
        self.assertEqual(response["data"][0]["room_number"], 1)
        self.assertEqual(response["data"][0]["guests"], 2)