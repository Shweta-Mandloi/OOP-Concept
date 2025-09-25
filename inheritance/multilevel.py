# Base class
class Primary:
    def __init__(self, name):
        self.name = name
    def show_primary(self):
        print(f"Name: {self.name}")

# Derived class (Secondary)
class Secondary(Primary):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def show_secondary(self):
        print(f"School: {self.school}")

# Derived class (College) → Multilevel Inheritance
class College(Secondary):
    def __init__(self, name, school, college, cgpa):
        super().__init__(name, school)
        self.college = college
        self.cgpa = cgpa
    def show_college(self):
        print(f"College: {self.college}, CGPA: {self.cgpa}")

# ================= Demo =================
c = College("Shweta Mandloi", "Maa Umiya School", "Sushila Devi Bansal College", 8.7)
c.show_primary()
c.show_secondary()
c.show_college()
