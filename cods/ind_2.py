class Literature:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"Я недавно прочёл книгу: '{self.title}'. Её написал  {self.author}.")


book = Literature("War of the Worlds", "Herbert Wells")
book.read()
