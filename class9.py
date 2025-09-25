# 9. Circle — Calculate Circumference

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
       ## pi = 3.14 
        return 2 * math.pi * self.radius

c = Circle(5)
print("Circumference:", round(c.circumference(), 2))
