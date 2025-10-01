class Vehicle:
    def __init__(self, speed):
        self.__speed = speed

    def set_speed(self, s):
        if s > 0:
            self.__speed = s
        else:
            print("Invalid speed")

    def get_speed(self):
        return self.__speed

v = Vehicle(60)
print("Speed:", v.get_speed())
v.set_speed(80)
print("Updated Speed:", v.get_speed())
