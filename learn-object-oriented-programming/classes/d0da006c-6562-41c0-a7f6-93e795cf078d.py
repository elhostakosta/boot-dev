class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for search_book in self.books:
            if search_book.title == book.title:
                self.books.remove(search_book)

    def search_books(self, search_string):
        matched_books = []
        search_string = search_string.lower()
        for book in self.books:
            if (search_string in book.title.lower() or search_string in book.author.lower()):
                matched_books.append(book)
        return matched_books
