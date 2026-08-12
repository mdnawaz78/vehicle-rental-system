class Vehicle:
    def __init__(self, vehicle_number, brand, rental_price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.rental_price = rental_price

    def display_details(self):
        print(f"Vehicle Number: {self.vehicle_number}")
        print(f"Brand: {self.brand}")
        print(f"Rental Price   : ₹{self.rental_price}/day")

    def calculate_rental_cost(self, days):
        return self.rental_price * days