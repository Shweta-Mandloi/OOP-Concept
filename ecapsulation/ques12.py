class Car:
    def __init__(self, fuel):
        self.__fuel = fuel

    def add_fuel(self, amount):
        if amount > 0:
            self.__fuel += amount
        else:
            print("Invalid fuel amount")

    def show_fuel(self):
        print("Fuel Level:", self.__fuel, "liters")

c = Car(50)
c.add_fuel(20)
c.show_fuel()
