class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return f"{self.r+other.r}+{self.i+other.i}i"

c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(c1 + c2)
