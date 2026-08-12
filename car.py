from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,vehicle_number,brand,rental_price,number_of_seats):
        super().__init__(vehicle_number,brand,rental_price)
        self.number_of_seats = number_of_seats

    def display_details(self):
        super().display_details()
        print(f"Number of Seats: {self.number_of_seats}")

    def calculate_rental_cost(self,days):
        total = self.rental_price * days
        if days >= 7:
            total =total * 0.90  # Apply a 10% discount for rentals longer than 7 days
        return total