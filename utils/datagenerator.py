test_data = {}

test_data['ep'] = {
    "valid": {"name": "Sebi1", "check_in": "2024-01-01", "check_out": "2024-01-02", "guests": 2, "room_number": 1},
    "wrong_check_in": {"name": "Sebi2", "check_in": "2024-01-06", "check_out": "2024-01-01", "guests": 2, "room_number": 2},
    "wrong_guests": {"name": "Sebi3", "check_in": "2024-01-01", "check_out": "2024-01-02", "guests": -1, "room_number": 3},
    "room_occupied": {"name": "Sebi4", "check_in": "2024-01-01", "check_out": "2024-01-07", "guests": 2, "room_number": 1}
}

test_data['bva'] = {
    "valid_1": {"name": "Sebi1", "check_in": "2024-01-01", "check_out": "2024-01-02", "guests": 5, "room_number": 1},
    "valid_2": {"name": "Sebi2", "check_in": "2024-01-01", "check_out": "2024-01-09", "guests": 1, "room_number": 2},
    "wrong_check_in": {"name": "Sebi3", "check_in": "2024-01-01", "check_out": "2024-01-01", "guests": 2, "room_number": 3},
    "wrong_guests": {"name": "Sebi4", "check_in": "2024-01-01", "check_out": "2024-01-02", "guests": 0, "room_number": 4}
}

test_data['ceg'] = {
    "valid": [
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-02", "guests": 2, "room_number": 1}
    ],
    "wrong_check_in": [
        {"name": "Sebi", "check_in": "2024-01-06", "check_out": "2024-01-01", "guests": 2, "room_number": 2},
        {"name": "Sebi", "check_in": "2024-01-06", "check_out": "2024-01-01", "guests": -1, "room_number": 2},
        {"name": "Sebi", "check_in": "2024-01-06", "check_out": "2024-01-01", "guests": 2, "room_number": 1},
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-01", "guests": 2, "room_number": 2},
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-01", "guests": 2, "room_number": 3},
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-01", "guests": 2, "room_number": 4},
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-01", "guests": 2, "room_number": 5},
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-01", "guests": 2, "room_number": 6}
    ],
    "wrong_guests": [
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-02", "guests": -1, "room_number": 3},
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-05", "guests": 0, "room_number": 1}
    ],
    "room_occupied": [
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-07", "guests": 2, "room_number": 1}
    ]
}

test_data['mcdc'] = {
    "valid": [
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-02", "guests": 1, "room_number": 1}
    ],
    "wrong_check_in": [
        {"name": "Sebi", "check_in": "2024-01-02", "check_out": "2024-01-01", "guests": 0, "room_number": 1},
        {"name": "Sebi", "check_in": "2024-01-02", "check_out": "2024-01-01", "guests": 0, "room_number": 2},
        {"name": "Sebi", "check_in": "2024-01-02", "check_out": "2024-01-01", "guests": 2, "room_number": 1},
        {"name": "Sebi", "check_in": "2024-01-02", "check_out": "2024-01-01", "guests": 2, "room_number": 2}
    ],
    "wrong_guests": [
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-04", "guests": 0, "room_number": 1},
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-04", "guests": 0, "room_number": 2}
    ],
    "room_occupied": [
        {"name": "Sebi", "check_in": "2024-01-01", "check_out": "2024-01-05", "guests": 2, "room_number": 1}
    ]
}