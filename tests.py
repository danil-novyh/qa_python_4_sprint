import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #2
    def test_add_new_book_long_name_not_added(self):
        collector = BooksCollector()
        long_name = "A" * 41  # 41 символ — больше лимита
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()    
    #3
    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()
    #4
    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        book = "Дубровский"
        collector.add_new_book(book)
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 1
    #5
    def test_add_new_book_no_genre_by_default(self):
        collector = BooksCollector()
        book = "Война и мир"
        collector.add_new_book(book)
        assert collector.get_book_genre(book) == ''
    #6
    @pytest.mark.parametrize("book,genre", [
        ("Детектив", "Детективы"),
        ("Звёздные войны", "Фантастика"),
        ("Микки Маус", "Мультфильмы")
    ])
    def test_set_and_get_book_genre_correct(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre
    #7
    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        book = "Книга без жанра"
        collector.add_new_book(book)
        collector.set_book_genre(book, "Неизвестный жанр")
        assert collector.get_book_genre(book) == ''
    #8
    def test_set_book_genre_nonexistent_book_not_set(self):
        collector = BooksCollector()
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert collector.get_book_genre("Несуществующая книга") is None
    #9
    def test_get_books_with_specific_genre_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book("Звёздные войны")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Звёздные войны", "Фантастика")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert set(books) == {"Звёздные войны", "Гарри Поттер"}
    #10
    def test_get_books_with_specific_genre_empty_for_invalid_genre(self):
        collector = BooksCollector()
        books = collector.get_books_with_specific_genre("Неизвестный жанр")
        assert books == []
    #11
    def test_get_books_for_children_excludes_age_rating_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Ужасы на Хэллоуин")
        collector.add_new_book("Том и Джерри")
        collector.set_book_genre("Ужасы на Хэллоуин", "Ужасы")
        collector.set_book_genre("Том и Джерри", "Мультфильмы")
        children_books = collector.get_books_for_children()
        assert "Том и Джерри" in children_books
        assert "Ужасы на Хэллоуин" not in children_books