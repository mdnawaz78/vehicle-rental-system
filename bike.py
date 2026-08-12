from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self,vehicle_number,brand,rental_price,engine_capacity):
        super().__init__(vehicle_number,brand,rental_price)
        self.engine_capacity = engine_capacity
    
    def display_details(self):
        super().display_details()
        print(f"Engine Capacity: {self.engine_capacity} cc")

    def calculate_rental_cost(self,days):
        total = self.rental_price * days
        if days >= 3:
            total = total * 0.95  # Apply a 5% discount for rentals of 3 or more days
        return total