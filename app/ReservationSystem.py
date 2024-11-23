from datetime import datetime

from utils.exceptions import *
from utils.response import ok_response


class ReservationSystem:
    def __init__(self):
        self.reservations = {}
        self.next_id = 1

    def add_reservation(self, name, check_in, check_out, room_number, guests):
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")

        if check_out_date <= check_in_date:
            raise InvalidCheckOutDate
        if guests < 1:
            raise InvalidNumberOfGuests

        # check overlapping reservations
        for res in self.reservations.values():
            if res["room_number"] == room_number and not (
                    check_out_date <= res["check_in"] or check_in_date >= res["check_out"]
            ):
                raise RoomAlreadyBookedException

        reservation_id = self.next_id
        self.reservations[reservation_id] = {
            "name": name,
            "check_in": check_in_date,
            "check_out": check_out_date,
            "room_number": room_number,
            "guests": guests,
        }
        self.next_id += 1
        return ok_response("Reservation created", self.reservations[reservation_id])

    def modify_reservation(self, reservation_id, **updates):
        if reservation_id not in self.reservations:
            raise ReservationNotFoundException

        res = self.reservations[reservation_id]
        if "check_in" in updates:
            updates["check_in"] = datetime.strptime(updates["check_in"], "%Y-%m-%d")
        if "check_out" in updates:
            updates["check_out"] = datetime.strptime(updates["check_out"], "%Y-%m-%d")

        res.update(updates)
        return ok_response("Reservation updated", data=self.reservations[reservation_id] )

    def delete_reservation(self, reservation_id):
        if reservation_id in self.reservations:
            del self.reservations[reservation_id]
            return ok_response("Reservation_deleted", data={"reservation_id": reservation_id})
        raise ReservationNotFoundException

    def get_reservations_for_date(self, date):
        date = datetime.strptime(date, "%Y-%m-%d")
        reservations = [ res for res in self.reservations.values() if res["check_in"] <= date < res["check_out"]]
        return ok_response("Reservations fetched.", reservations)

    def get_all_reservations(self):
        return ok_response("Reservations fetched.", self.reservations)
