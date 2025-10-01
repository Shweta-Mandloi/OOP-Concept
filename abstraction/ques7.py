from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def grade(self):
        pass

class Test(Student):
    def grade(self):
        print("Grade: A")

t = Test()
t.grade()
