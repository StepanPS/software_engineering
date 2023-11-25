class Literature:
    def __init__(self, title, author, date):
        self.title = title
        self._author = author
        self.__date = date

    def read(self):
        print(f"Я недавно прочёл книгу: '{self.title}'. Её написал {self._author} в {self.__date} году.")


book = Literature("War of the Worlds", "Herbert Wells", 1898)
book.read()
print(book.title)
print(book._author)
print(book.__date)
