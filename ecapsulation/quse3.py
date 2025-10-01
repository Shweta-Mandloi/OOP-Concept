class Marks:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, m):
        if 0 <= m <= 100:
            self.__marks = m
        else:
            print("Invalid marks!")

    def get_marks(self):
        return self.__marks

s = Marks(85)
print("Marks:", s.get_marks())
s.set_marks(95)
print("Updated Marks:", s.get_marks())
