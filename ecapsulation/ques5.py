class Employee:
    def __init__(self, salary):
        self._salary = salary   # protected

class Manager(Employee):
    def show_salary(self):
        print("Manager Salary:", self._salary)

m = Manager(100000)
m.show_salary()
