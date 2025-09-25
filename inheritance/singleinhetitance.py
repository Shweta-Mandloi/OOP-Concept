# Base class
class Primary:
    def __init__(self, name):
        self.name = name
    def show_primary(self):
        print(f"Name: {self.name}")

# Derived class (Single Inheritance)
class Secondary(Primary):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def show_secondary(self):
        print(f"School: {self.school}")

# ================= Demo =================
s = Secondary("Shweta Mandloi", "Maa Umiya School")
s.show_primary()
s.show_secondary()
