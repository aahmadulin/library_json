import json
from os.path import exists
from library import Library, Book

def load_books_from_file(filename):
    if exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_books_to_file(library, filename):
    with open(filename, 'w') as f:
        json.dump(library.get_all_books(), f)

def main():
    library = Library()
    books_data = load_books_from_file('books.json')
    
    for book_data in books_data:
        try:
            # Пробуем создать книгу из загруженных данных
            book = Book(**book_data)
            library.add_book(book)
        except ValueError as e:
            print(f"Ошибка при загрузке книги: {e}")

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year_input = input("Введите год издания: ")
            
            try:
                # Пробуем преобразовать год в целое число
                year = int(year_input)  # Преобразуем ввод в целое число
                
                # Создаем объект Book
                book = Book(title=title, author=author, year=year)
                library.add_book(book)
                print("Книга успешно добавлена!")
            
            except ValueError as e:
                print(f"Ошибка: {e}")  # Обработка ошибки и вывод сообщения

        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)
        
        elif choice == '3':
            search_term = input("Введите название, автора или год для поиска: ")
            results = library.search_books(search_term)
            for result in results:
                print(result)

        elif choice == '4':
            all_books = library.get_all_books()
            for book in all_books:
                print(book)

        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(book_id, new_status)

        elif choice == '0':
            save_books_to_file(library, 'books.json')
            break

if __name__ == "__main__":
    main()
