class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display(self):
        print("Name:", self.name, "Age:", self.__age)

p = Person("Shweta", 20)
p.display()
