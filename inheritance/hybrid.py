class Primary:
    def __init__(self, name):
        self.name = name
       # print(self.name)

class Secondary(Primary):
    def __init__(self, name, school):
        Primary.__init__(self, name )
        self.school = school
 
# s = Secondary("shweta",'maa umiya gyanpeeth')

class College(Secondary):
     def __init__(self, name, school, college, cgpa):
         Secondary.__init__(self,name, school)   # chain continue hoti hai
         self.college = college
         self.cgpa = cgpa

class Company(Primary):
    def __init__(self, name, company, package):
        Primary.__init__(self,name)   # sirf name Primary ko jayega
        self.company = company
        self.package = package

class HybridPlacement(College, Company):
    def __init__(self, name, school, college, cgpa, company, package):
        College.__init__(self, name, school, college, cgpa)   # ✅ College ka constructor
        Company.__init__(self, name, company, package)        # ✅ Company ka constructor

    def show(self):
        print(f"Name: {self.name}")
        print(f"School: {self.school}")
        print(f"College: {self.college}")
        print(f"CGPA: {self.cgpa}")
        print(f"Company: {self.company}")
        print(f"Package: {self.package} LPA")

# Demo
hp = HybridPlacement("Shweta Mandloi", "Maa Umiya School",
                     "Sushila Devi Bansal College", 8.7,
                     "Google", 45)
hp.show()
