from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print("Manager salary is 50000")

m = Manager()
m.salary()
