class Phone:
    def feature(self):
        print("Basic calling feature")

class SmartPhone(Phone):
    def feature(self):
        print("Smartphone has internet and apps")

ph = Phone()
sp = SmartPhone()

ph.feature()
sp.feature()
