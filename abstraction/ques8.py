from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

class Guitar(Instrument):
    def play(self):
        print("Guitar is strumming")

g = Guitar()
g.play()
