# Base class 1
class Primary:
    def __init__(self, name):
        self.name = name
    def show_primary(self):
        print(f"Name: {self.name}")

# Base class 2
class Sports:
    def __init__(self, sport):
        self.sport = sport
    def show_sport(self):
        print(f"Favourite Sport: {self.sport}")

# Derived class → Multiple Inheritance
class StudentAthlete(Primary, Sports):
    def __init__(self, name, sport):
        Primary.__init__(self, name)
        Sports.__init__(self, sport)
    def show_athlete(self):
        print(f"{self.name}, Sport: {self.sport}")

# ================= Demo =================
athlete = StudentAthlete("Shweta Mandloi", "Kabbadi")
athlete.show_primary()
athlete.show_sport()
athlete.show_athlete()
