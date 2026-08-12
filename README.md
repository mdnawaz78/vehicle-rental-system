# Vehicle Rental System

A simple Python-based Vehicle Rental System developed using Object-Oriented Programming (OOP) concepts.

The application allows users to view available vehicles, search for a vehicle using its vehicle number, enter a rental duration, and calculate the total rental cost based on vehicle-specific rental rules.

---

## Project Overview

The Vehicle Rental System is designed to demonstrate the practical use of Object-Oriented Programming in Python.

The system supports two types of vehicles:

- Cars
- Bikes

A common `Vehicle` base class contains the properties and functionality shared by all vehicles. The `Car` and `Bike` classes inherit from `Vehicle` and implement their own vehicle-specific properties and rental discount rules.

The `RentalSystem` class manages the available vehicles, searches for vehicles, displays vehicle information, and handles rental calculations.

---

## Features

- Add multiple vehicles to the rental system
- Support for Cars and Bikes
- Display all available vehicles
- Search vehicles using vehicle number
- Calculate rental cost based on rental duration
- Different rental rules for Cars and Bikes
- Automatic rental discounts
- Case-insensitive vehicle search
- Input validation
- Handles invalid vehicle numbers
- Handles zero or negative rental duration
- Handles non-numeric rental duration
- Displays a rental summary after successful calculation

---

## Vehicle Rental Rules

### Car

- Rental price is calculated on a per-day basis.
- Rentals of **7 or more days** receive a **10% discount**.

Example:

```text
Rental Price = ₹1500/day
Duration = 7 days

Base Cost = ₹1500 × 7
          = ₹10500

10% Discount = ₹1050

Final Cost = ₹9450
```

### Bike

- Rental price is calculated on a per-day basis.
- Rentals of **3 or more days** receive a **5% discount**.

Example:

```text
Rental Price = ₹500/day
Duration = 5 days

Base Cost = ₹500 × 5
          = ₹2500

5% Discount = ₹125

Final Cost = ₹2375
```

---

## OOP Concepts Used

### 1. Classes and Objects

The project uses the following classes:

- `Vehicle`
- `Car`
- `Bike`
- `RentalSystem`

Objects are created from these classes to represent vehicles and manage the rental system.

---

### 2. Inheritance

`Car` and `Bike` inherit from the `Vehicle` class.

```text
Vehicle
├── Car
└── Bike
```

This allows common vehicle properties and methods to be reused.

For example:

```python
class Car(Vehicle):
```

and:

```python
class Bike(Vehicle):
```

---

### 3. Constructor

The `__init__()` method is used to initialize object attributes.

The `Vehicle` class initializes:

- Vehicle number
- Brand
- Rental price

The `Car` class additionally initializes:

- Number of seats

The `Bike` class additionally initializes:

- Engine capacity

---

### 4. Method Overriding

Both `Car` and `Bike` override methods inherited from the `Vehicle` class.

For example:

```python
def calculate_rental_cost(self, days):
```

The `Car` class applies a 10% discount for rentals of 7 or more days, while the `Bike` class applies a 5% discount for rentals of 3 or more days.

---

### 5. Polymorphism

The `RentalSystem` works with different vehicle objects through their common behavior.

When:

```python
vehicle.calculate_rental_cost(days)
```

is called, Python automatically executes the appropriate implementation based on the actual object.

For example:

- A `Car` object uses `Car.calculate_rental_cost()`
- A `Bike` object uses `Bike.calculate_rental_cost()`

This allows the rental system to work with different vehicle types without writing separate calculation logic for each type.

---

### 6. Encapsulation

Related data and behavior are grouped inside their respective classes.

For example, vehicle information and vehicle-related methods are contained within the `Vehicle`, `Car`, and `Bike` classes.

---

### 7. Code Reusability

The `Vehicle` base class provides common functionality that can be reused by both `Car` and `Bike`.

The `super()` function is used in the child classes to reuse the parent class constructor and methods.

---

## Project Architecture

```text
                         main.py
                            |
                            v
                     RentalSystem
                            |
                  manages vehicle objects
                            |
                 +----------+----------+
                 |                     |
                 v                     v
                Car                   Bike
                 |                     |
                 +----------+----------+
                            |
                         inherits
                            |
                            v
                         Vehicle
```

### Responsibility of Each Component

```text
Vehicle
    |
    └── Contains common vehicle properties and methods

Car
    |
    └── Adds number of seats and car-specific rental rules

Bike
    |
    └── Adds engine capacity and bike-specific rental rules

RentalSystem
    |
    └── Stores, searches, displays, and manages vehicles

main.py
    |
    └── Creates objects and handles user interaction
```

---

## Project Structure

```text
vehicle-rental-system/
│
├── vehicle.py
├── car.py
├── bike.py
├── rental_system.py
├── main.py
├── README.md
└── .gitignore
```

### File Description

| File | Purpose |
|---|---|
| `vehicle.py` | Contains the base `Vehicle` class and common vehicle functionality |
| `car.py` | Contains the `Car` class and car-specific rental rules |
| `bike.py` | Contains the `Bike` class and bike-specific rental rules |
| `rental_system.py` | Manages vehicles, vehicle searching, and rental calculations |
| `main.py` | Entry point of the application and handles user interaction |
| `README.md` | Project documentation |
| `.gitignore` | Specifies files that should not be tracked by Git |

---

## Sample Vehicles

The application currently includes the following vehicles:

| Vehicle Number | Type | Brand | Rental Price | Additional Information |
|---|---|---|---:|---|
| CAR001 | Car | Toyota | ₹1500/day | 5 seats |
| CAR002 | Car | Honda | ₹1800/day | 7 seats |
| BIKE001 | Bike | Yamaha | ₹500/day | 150 cc |
| BIKE002 | Bike | Royal Enfield | ₹800/day | 350 cc |

---

## How to Run

### Requirements

- Python 3.x
- No external Python packages are required.

### Steps

1. Clone or download the repository.
2. Open the project folder in a terminal.
3. Run the following command:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

The application will display the available vehicles and ask the user to enter a vehicle number and rental duration.

---

## Example Output

```text
===== AVAILABLE VEHICLES =====

Vehicle Number: CAR001
Brand: Toyota
Rental Price   : ₹1500/day
Number of Seats: 5

Vehicle Number: CAR002
Brand: Honda
Rental Price   : ₹1800/day
Number of Seats: 7

Vehicle Number: BIKE001
Brand: Yamaha
Rental Price   : ₹500/day
Engine Capacity: 150 cc

Vehicle Number: BIKE002
Brand: Royal Enfield
Rental Price   : ₹800/day
Engine Capacity: 350 cc

===== RENT A VEHICLE =====
Enter vehicle number: CAR001
Enter rental duration in days: 7

===== RENTAL SUMMARY =====
Vehicle Number : CAR001
Rental Duration: 7 days
Total Amount   : ₹9450.00
```

---

## Input Validation and Error Handling

The application handles common invalid inputs.

### Invalid Vehicle Number

```text
===== RENT A VEHICLE =====
Enter vehicle number: ABC999
Enter rental duration in days: 5
Vehicle 'ABC999' not found.
```

### Non-Numeric Rental Duration

```text
===== RENT A VEHICLE =====
Enter vehicle number: CAR001
Enter rental duration in days: ABC
Please enter a valid number for rental duration.
```

### Zero or Negative Rental Duration

```text
===== RENT A VEHICLE =====
Enter vehicle number: CAR001
Enter rental duration in days: -5
Rental duration must be greater than 0 days.
```

The vehicle search is also case-insensitive, so entering `car001` can match `CAR001`.

---

## Technologies Used

- Python 3
- Object-Oriented Programming
- Git
- GitHub

---

## Design Approach

The project follows a simple object-oriented design.

Common vehicle properties and behavior are placed in the `Vehicle` base class. `Car` and `Bike` extend the base class with their own properties and rental rules.

The `RentalSystem` is responsible for managing vehicle objects, while `main.py` handles the application flow and user interaction.

This separation keeps the code organized, reusable, and easy to understand.

---

## Future Improvements

Possible improvements for a larger version of the application could include:

- Customer management
- Vehicle availability status
- Rental history
- Return vehicle functionality
- Database integration
- Graphical or web-based user interface
- Persistent storage of vehicle and rental information

These features are outside the scope of the current assessment.

---

## Author

**Md Nawaz Sharif Khan**