class Literature:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"Я недавно прочёл книгу: '{self.title}'. Её написал  {self.author}.")


book = Literature("War of the Worlds", "Herbert Wells")
book.read()


class Film(Literature):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def fiction(self):
        return f"Нет же! '{self.title}' это фильм режиссёра {self.author} выпущенный в {self.genre} году."


fiction_book = Film("War of the Worlds", "Steven Spielberg", 2005)
print(fiction_book.fiction())
