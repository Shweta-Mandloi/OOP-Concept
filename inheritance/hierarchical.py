# Base class
class Primary:
    def __init__(self, name):
        self.name = name
    def show_primary(self):
        print(f"Name: {self.name}")

# Derived class 1 → Hierarchical
class Company(Primary):
    def __init__(self, name, company, package):
        super().__init__(name)
        self.company = company
        self.package = package
    def show_company(self):
        print(f"Company: {self.company}, Package: {self.package} LPA")

# ================= Demo =================
comp = Company("Shweta Mandloi", "Google", 45)
comp.show_primary()
comp.show_company()
