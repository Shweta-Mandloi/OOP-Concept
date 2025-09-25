#calculator - add and subtract

class Calculator:
    def add(self, a, b):
        return a + b 
    
    def subtract(self, a, b):
        return a - b
    
calc = Calculator()
print("5 + 6 =", calc.add(5, 6))
print("10 - 8 =", calc.subtract(10, 8))