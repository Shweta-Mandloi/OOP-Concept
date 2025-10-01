from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def taste(self):
        pass

class Pizza(Food):
    def taste(self):
        print("Pizza is cheesy")

p = Pizza()
p.taste()
