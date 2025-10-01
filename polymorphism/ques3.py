class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return "Area = πr²"

class Rectangle(Shape):
    def area(self):
        return "Area = l × b"

for s in [Circle(), Rectangle()]:
    print(s.area())


