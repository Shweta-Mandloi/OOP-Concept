##Temperature — Celsius to Fahrenheit

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.to_fahrenheit()}°F")
