class Student:
    def __init__(self, name):
        self.__name = name   # private

    def show_name(self):
        print("Student Name:", self.__name)

s = Student("Shweta")
s.show_name()
