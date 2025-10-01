class Dog:
    def speak(self): print("Bark")

class Cat:
    def speak(self): print("Meow")

for animal in [Dog(), Cat()]:
    animal.speak()
