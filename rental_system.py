class RentalSystem:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles available.")
            return

        print("\n===== AVAILABLE VEHICLES =====")

        for vehicle in self.vehicles:
            print()
            vehicle.display_details()

    def find_vehicle(self, vehicle_number):
        for vehicle in self.vehicles:
            if vehicle.vehicle_number.lower() == vehicle_number.lower():
                return vehicle

        return None

    def calculate_rental(self, vehicle_number, days):
        if days <= 0:
            print("Rental duration must be greater than 0 days.")
            return None

        vehicle = self.find_vehicle(vehicle_number)

        if vehicle is None:
            print(f"Vehicle '{vehicle_number}' not found.")
            return None

        return vehicle.calculate_rental_cost(days)