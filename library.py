class Book:
    def __init__(self, title, author, year, status="в наличии", id=None):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author} ({self.year}) - {self.status}"

class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, book):
        book.id = self.next_id
        self.books.append(book)
        self.next_id += 1

    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, term):
        results = [book for book in self.books if term.lower() in book.title.lower() or 
                   term.lower() in book.author.lower() or 
                   term.lower() in str(book.year)]
        return results

    def get_all_books(self):
        return [book.to_dict() for book in self.books]

    def change_status(self, book_id, new_status):
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                else:
                    print("Неверный статус. Доступные статусы: 'в наличии', 'выдана'.")
                return
        print(f"Книга с ID {book_id} не найдена.")