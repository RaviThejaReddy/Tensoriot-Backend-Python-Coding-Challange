from src.car import Car
import pytest
from unittest.mock import MagicMock

def test_park():
    parking_lot = MagicMock()
    car = Car("ABC1234")
    result = car.park(parking_lot, 0)
    parking_lot.park_car.assert_called_once_with(car, 0)
    assert result == parking_lot.park_car.return_value

def test_invalid_licenese():
    with pytest.raises(ValueError):
        car = Car("ABC123")
