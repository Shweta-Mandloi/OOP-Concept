## 5. Student — Calculate Average Marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student("Bob", [80, 90, 85])
print(f"{s.name}'s average: {s.average()}")

