import json
from faker import Faker
import random

fake = Faker()


def generate_owners_and_related_data(num_owners):
    owners = []
    cars = []
    statuses = []

    for i in range(1, num_owners + 1):
        # Generate owner
        owner = {
            "model": "core.owner",  # Change 'core' to your actual app name
            "pk": i,
            "fields": {
                "rfid": f"RFID{i:04d}",
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "phone_number": fake.phone_number(),
                # Optionally add profile_photo if needed
            },
        }
        owners.append(owner)

        # Generate vehicle status
        status = {
            "model": "core.vehiclestatus",  # Change 'core' to your actual app name
            "pk": i,  # Use the same ID as the car to ensure a one-to-one relationship
            "fields": {
                "status": random.choice(["in", "out"]),
            },
        }
        statuses.append(status)

        # Generate car for the owner
        car = {
            "model": "core.car",  # Change 'core' to your actual app name
            "pk": i,
            "fields": {
                "owner": i,  # Reference to the owner
                "make": fake.company(),
                "model": fake.word(),
                "license_plate": fake.license_plate(),
                "vehicle_status": i,  # Reference to the vehicle status
                # Optionally add photo if needed
            },
        }
        cars.append(car)

    return owners, cars, statuses


def main():
    num_owners = 50

    owners, cars, statuses = generate_owners_and_related_data(num_owners)

    # Combine all data into a single list
    data = owners + cars + statuses

    # Write to a JSON file
    with open("initial_data.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
