import random
import string

def GenerateCars(Car, no_of_cars):
    print(f'Generating {no_of_cars} Cars Randomly')
    existing_plates = set()
    cars = []
    for _ in range(no_of_cars):
        license_plate = GenerateLicensePlate(existing_plates)
        existing_plates.add(license_plate)
        cars.append(Car(license_plate))
    print(f'Generated {no_of_cars} Cars Randomly\n\n')
    return cars


def GenerateLicensePlate(existing_plates, no_of_digits=7):
    if no_of_digits < 1:
        raise ValueError("Number of digits must be at least 1")

    while True:
        letters_part = ''.join(random.choices(string.ascii_uppercase, k=3))
        digits_part = ''.join(random.choices(string.digits, k=no_of_digits - 3))
        license_plate = letters_part + digits_part
        if license_plate not in existing_plates:
            return license_plate