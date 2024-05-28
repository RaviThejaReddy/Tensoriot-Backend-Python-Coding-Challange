class Car:
    """
    Create a car class that takes in a 7 digit license plate and sets it as a property. The car will have 2 methods:
    - A magic method to output the license plate when converting the class instance to a
    string.
    - A "park" method that will take a parking lot and spot # as input and fill in the
    selected spot in the parking lot. If another car is parked in that spot, return a status
    indicating the car was not parked successfully. If no car is parked in that spot, return a
    status indicating the car was successfully parked.
        """
    def __init__(self, license_plate):
        if len(license_plate) != 7:
            raise ValueError("License plate must be 7 characters long")
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot, spot_num):
        return parking_lot.park_car(self, spot_num)