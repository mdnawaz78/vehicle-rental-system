from car import Car
from bike import Bike
from rental_system import RentalSystem


# Creating rental system
rental_system = RentalSystem()


# Creating vehicles
car1 = Car("CAR001", "Toyota", 1500, 5)
car2 = Car("CAR002", "Honda", 1800, 7)

bike1 = Bike("BIKE001", "Yamaha", 500, 150)
bike2 = Bike("BIKE002", "Royal Enfield", 800, 350)


# Adding vehicles to the rental system
rental_system.add_vehicle(car1)
rental_system.add_vehicle(car2)
rental_system.add_vehicle(bike1)
rental_system.add_vehicle(bike2)


# Displaying available vehicles
rental_system.display_all_vehicles()


# Taking user input
print("\n===== RENT A VEHICLE =====")

vehicle_number = input("Enter vehicle number: ").strip()

try:
    days = int(input("Enter rental duration in days: "))

    total = rental_system.calculate_rental(vehicle_number, days)

    if total is not None:
        print("\n===== RENTAL SUMMARY =====")
        print(f"Vehicle Number : {vehicle_number}")
        print(f"Rental Duration: {days} days")
        print(f"Total Amount   : ₹{total:.2f}")

except ValueError:
    print("Please enter a valid number for rental duration.")