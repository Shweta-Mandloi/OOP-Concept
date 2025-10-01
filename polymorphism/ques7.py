class Appliance:
    def power(self):
        print("General appliance power")

class Fan(Appliance):
    def power(self):
        print("Fan uses 60W")

class AC(Appliance):
    def power(self):
        print("AC uses 2000W")

a = Appliance()
f = Fan()
ac = AC()

a.power()
f.power()
ac.power()
