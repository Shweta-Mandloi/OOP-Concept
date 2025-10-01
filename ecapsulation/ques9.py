class Teacher:
    def __init__(self, subject):
        self.__subject = subject

    def show_subject(self):
        print("Teacher Subject:", self.__subject)

t = Teacher("Math")
t.show_subject()
