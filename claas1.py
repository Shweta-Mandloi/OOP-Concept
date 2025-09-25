class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, \nAge: {self.age}")

p = Person("shweta mandloi", 20)
p.display()
