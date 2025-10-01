class Student:
    def __init__(self, roll_no):
        self.__roll_no = roll_no

    def get_roll_no(self):
        return self.__roll_no

s = Student(189)
print("Roll No:", s.get_roll_no())
