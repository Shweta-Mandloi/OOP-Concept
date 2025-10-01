from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod
    def color(self):
        pass

class Apple(Fruit):
    def color(self):
        print("Apple is Red")

a = Apple()
a.color()
