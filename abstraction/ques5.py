from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):
    def interest(self):
        print("SBI interest = 4%")

s = SBI()
s.interest()
