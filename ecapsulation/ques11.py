class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def show_info(self):
        print(f"'{self.__title}' by {self.__author}")

b = Book("my life story", "shweta mandloi")
b.show_info()
