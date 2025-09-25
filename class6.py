## 6. Car — Start and Stop
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.is_running = False   # car shuru me band hai

    def start(self):
        if self.is_running:  # agar already chal rahi hai
            print(f"{self.brand} is already running!")
        else:
            self.is_running = True
            print(f"{self.brand} started.")

    def stop(self):
        if not self.is_running:  # agar already band hai
            print(f"{self.brand} is already stopped!")
        else:
            self.is_running = False
            print(f"{self.brand} stopped.")


car = Car("Toyota")
car.start()   # pehli baar start hogi
car.start()   # dusri baar bolega already running
car.stop()    # pehli baar band hogi
car.stop()    # dusri baar bolega already stopped


