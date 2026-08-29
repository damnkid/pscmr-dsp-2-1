# Base Class
class Vehicle:
    def description(self):
        print("This is a vehicle")


# Derived Class - Car
class Car(Vehicle):
    def description(self):
        print("This is a car")


# Derived Class - Bike
class Bike(Vehicle):
    def description(self):
        print("This is a bike")


# Main Program
v = Vehicle()
c = Car()
b = Bike()

v.description()  # Parent method
c.description()  # Overridden in Car
b.description()  # Overridden in Bike
