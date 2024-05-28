import random

from parking_lot import ParkingLot
from car import Car
from generate_cars_with_licenses_plates import GenerateCars


def main(square_footage, parking_spot_width, parking_spot_length):
    """
    Have a main method take an array of cars with random license plates and have them park in a random spot in the parking lot array until the input array is empty or the parking lot is full.
    If a car tries to park in an occupied spot, have it try to park in a different spot instead until it successfully parks. 
    Once the parking lot is full, exit the program.

    this method takes in square_footage, parking_spot_width, parking_spot_length
    and generate cars randomly from 0 to no of parking spots +1
    and then try's to park them randomly

    at the end maps the parking spots with cars and saves the json to local and then upload to s3 bucket
    """
    parking_lot = ParkingLot(square_footage, parking_spot_width, parking_spot_length)
    print(f'No of parking spots available {parking_lot.num_of_parking_spots}')
    
    # Create an array of cars with random license plates
    cars = GenerateCars(Car, random.randint(0, parking_lot.num_of_parking_spots + 1))

    # Randomly park cars until the parking lot is full or all cars are parked
    for car in cars:
        while True:
            spot_num = random.randint(0, parking_lot.num_of_parking_spots - 1)
            if not parking_lot.is_full():
                result = car.park(parking_lot, spot_num)
                if ("successfully" in result) or parking_lot.is_full():
                    print(result)
                    break
                else:
                    print(result)
            else:
                print("Parking lot is full")
                break

    # Optionally save the parking map to a JSON file
    parking_lot.map_vehicles_to_parked_spots_json('parking_lot_map.json', '<REPLACE THIS WITH BUCKET NAME>')


if __name__ == "__main__":
    square_footage = 2000
    parking_spot_width = 8
    parking_spot_length = 12
    main(square_footage, parking_spot_width, parking_spot_length)
