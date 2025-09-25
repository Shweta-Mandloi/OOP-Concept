
class Dog: # We define a class called "Dog"
    species = "Canis familiaris" # A class attribute
    def __init__(self, name, breed):  # The constructor (explained later)
         self.name = name     # An instance attribute to store the dog's name
         self.breed = breed   # An instance attribute to store the dog's breed
    def bark(self): # A method (an action the dog can do)
         print(f"{self.name} says Woof!")
 # Now, let's create some Dog objects:

my_dog = Dog("Buddy","Golden Retriever") # Creating an object called my_dog
another_dog = Dog("Lucy","Labrador") # Creating another object

 # We can access their attributes:
print(my_dog.name) # Output: Buddy
print(another_dog.breed) # Output: Labrador
 # And make them perform actions:
my_dog.bark() # Output: Buddy says Woof!
print(Dog.species) # Output: Canis familiaris


class Car:
       def __init__(self , name ,color):
              self.name = name 
              self.color = color
       def my_car(self):
            print("my fav car" , self.name , self.color)

    # Creating objects
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

# Using objects
car1.my_car()   
car2.my_car()   
              