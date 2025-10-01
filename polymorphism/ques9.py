class Vehicle:
    def speed(self):
        print("Vehicle speed normal")

class Car(Vehicle):
    def speed(self):
        print("Car speed 100 km/h")

class Bike(Vehicle):
    def speed(self):
        print("Bike speed 80 km/h")

v = Vehicle()
c = Car()
b = Bike()

v.speed()
c.speed()
b.speed()
