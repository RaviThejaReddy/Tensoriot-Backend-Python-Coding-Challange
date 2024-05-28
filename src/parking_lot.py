import json
import boto3

s3 = boto3.client('s3')


class ParkingLot:
    """
    Create a parking lot class that takes in a square footage size as input and creates an array of empty values based on the input square footage size. 
    Assume every parking spot is 8x12 (96 ft2) for this program, but have the algorithm that calculates the array size be able to account for different parking spot sizes. 
    For example, a parking lot of size 2000ft2 can fit 20 cars, but if the parking spots were 10x12 (120 ft2), it could only fit 16 cars. 
    The size of the array will determine how many cars can fit in the parking lot.
    """

    def __init__(self, square_footage_size, parking_spot_width=8, parking_spot_length=12):
        self.square_footage_size = square_footage_size
        self.parking_spot_width = parking_spot_width
        self.parking_spot_length = parking_spot_length
        self.parking_spot_size = parking_spot_width * parking_spot_length
        self.num_of_parking_spots = square_footage_size // self.parking_spot_size
        self.parking_spots = [None] * self.num_of_parking_spots

    def park_car(self, car, spot_num):
        """
        checks if the parking spot is valid
        and if empty parks the car, else returns error
        """
        if 0 <= spot_num < self.num_of_parking_spots:
            if self.parking_spots[spot_num] is None:
                self.parking_spots[spot_num] = car
                return f"Car with license plate {car.license_plate} parked successfully in spot {spot_num}."
            else:
                return f"Spot {spot_num} is already occupied."
        else:
            return f"Spot {spot_num} is invalid."

    def is_full(self):
        """
        checks if all the parking spots are full
        """
        return all(spot is not None for spot in self.parking_spots)

    def map_vehicles_to_parked_spots_json(self, filename, s3_bucket_name):
        """
        maps cars to parked spots and writes the data in json format to local and then upload its to s3 bucket
        """
        vehicle_map = {str(i): str(car) for i, car in enumerate(
            self.parking_spots) if car is not None}
        with open(filename, 'w') as f:
            json.dump(vehicle_map, f)
            f.close()
        with open(filename, 'rb') as f:
            s3.upload_fileobj(f, s3_bucket_name, filename)
            f.close()
