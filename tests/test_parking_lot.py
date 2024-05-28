import pytest
import json
from unittest.mock import patch, mock_open
from src.car import Car
from src.parking_lot import ParkingLot

@pytest.fixture
def parking_lot():
    return ParkingLot(square_footage_size=960, parking_spot_width=8, parking_spot_length=12)

def test_initialization(parking_lot):
    assert parking_lot.square_footage_size == 960
    assert parking_lot.parking_spot_width == 8
    assert parking_lot.parking_spot_length == 12
    assert parking_lot.parking_spot_size == 96
    assert parking_lot.num_of_parking_spots == 10
    assert len(parking_lot.parking_spots) == 10
    assert all(spot is None for spot in parking_lot.parking_spots)

def test_park_car(parking_lot):
    car1 = Car("ABC1234")
    result = parking_lot.park_car(car1, 0)
    assert result == "Car with license plate ABC1234 parked successfully in spot 0."
    assert parking_lot.parking_spots[0] == car1

    # Test parking in the same spot
    car2 = Car("XYZ5678")
    result = parking_lot.park_car(car2, 0)
    assert result == "Spot 0 is already occupied."
    assert parking_lot.parking_spots[0] == car1

    # Test invalid spot number
    result = parking_lot.park_car(car2, 11)
    assert result == "Spot 11 is invalid."

def test_is_full(parking_lot):
    for i in range(parking_lot.num_of_parking_spots):
        car = Car(f"CAR{i}123")
        parking_lot.park_car(car, i)
    assert parking_lot.is_full()

    parking_lot.parking_spots[0] = None
    assert not parking_lot.is_full()

@patch("builtins.open", new_callable=mock_open)
@patch("json.dump")
def test_map_vehicles_to_parked_spots_json(mock_json_dump, mock_file_open, parking_lot):
    car1 = Car("ABC1234")
    car2 = Car("XYZ5678")
    parking_lot.park_car(car1, 0)
    parking_lot.park_car(car2, 1)

    filename = "test_parking_lot_map.json"
    s3_bucket_name = "test_bucket"
    parking_lot.map_vehicles_to_parked_spots_json(filename, s3_bucket_name)

    mock_file_open.assert_called_once_with(filename, 'w')
    expected_data = {
        "0": "ABC1234",
        "1": "XYZ5678"
    }
    mock_json_dump.assert_called_once_with(expected_data, mock_file_open())

if __name__ == "__main__":
    pytest.main()
