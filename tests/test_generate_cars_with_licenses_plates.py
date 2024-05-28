import pytest
from src.car import Car
from src.generate_cars_with_licenses_plates import GenerateCars, GenerateLicensePlate

@pytest.mark.parametrize("no_of_cars", [0, 1, 5])
def test_generate_cars(no_of_cars):
    cars = GenerateCars(Car, no_of_cars)
    assert len(cars) == no_of_cars
    for car in cars:
        assert isinstance(car, Car)

def test_generate_license_plate():
    existing_plates = {"ABC1234", "XYZ5678"}  # Some existing plates
    no_of_digits = 7

    # Generate a license plate
    license_plate = GenerateLicensePlate(existing_plates, no_of_digits)
    assert len(license_plate) == no_of_digits
    assert license_plate not in existing_plates

def test_generate_license_plate_invalid_input():
    # Test with negative number of digits
    with pytest.raises(ValueError):
        GenerateLicensePlate(set(), -1)

    # Test with zero number of digits
    with pytest.raises(ValueError):
        GenerateLicensePlate(set(), 0)
