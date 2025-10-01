from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def operation(self):
        pass

class Adder(Calculator):
    def operation(self):
        print("Performs addition")

a = Adder()
a.operation()
