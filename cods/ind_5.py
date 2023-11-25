class Magazine:
    def __init__(self, title, publisher):
        self.title = title
        self.publisher = publisher

    def display_info(self):
        return f"Журнал'{self.title}' издаётся {self.publisher}."


class Literature:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Книга '{self.title}' написана {self.author}."


class Bookshelf:
    def show_item_info(self, item):
        return item.display_info()


fiction_book = Literature("War of the Worldsd", "Herbert Wells")
magazine = Magazine("National Geographic", "National Geographic Partners")
bookshelf = Bookshelf()

print(bookshelf.show_item_info(fiction_book))
print(bookshelf.show_item_info(magazine))
