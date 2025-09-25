#  Dog - 
class Dog:
    def __init__(self , name , bark):
        self.name = name
        self.bark = bark 

    def sound(self):
        print(f"name: {self.name} and sound {self.bark}")

s = Dog("tomii" , "woof")
s.sound()