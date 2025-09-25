## 8. Book — Display Title and Author

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"'{self.title}' by {self.author}")

book = Book("My life story", "Shweta Mandloi")
book.info()

