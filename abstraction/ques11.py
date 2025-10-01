from abc import ABC, abstractmethod

class Book(ABC):
    @abstractmethod
    def info(self):
        pass

class Novel(Book):
    def info(self):
        print("Title: 1984, Author: George Orwell")

b = Novel()
b.info()
