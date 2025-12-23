# library.py
from models.book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author, year):
        new_book = Book(name, author, year)
        self.books.append(new_book)
        print(f"Kitap başarıyla eklendi: {new_book}")

    def remove_book(self, name):
        for book in self.books:
            if book.name.lower() == name.lower():
                self.books.remove(book)
                print(f"Kitap başarıyla silindi: {book}")
                return
        print("Kitap bulunamadı.")

    def search_by_name(self, name):
        results = [book for book in self.books if name.lower() in book.name.lower()]
        if results:
            print("\nArama Sonuçları:")
            for book in results:
                print(book)
        else:
            print("Aranan kitap bulunamadı.")

    def search_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        if results:
            print(f"\n{author} yazarı için bulunan kitaplar:")
            for book in results:
                print(book)
        else:
            print("Bu yazara ait kitap bulunamadı.")

    def list_books(self):
        if not self.books:
            print("Kütüphanede hiç kitap yok.")
            return

        print("\nKütüphanedeki Kitaplar:")
        for book in self.books:
            print(book)