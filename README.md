# qa_python_4_sprint
1. test_add_new_book_add_two_books
Проверяет, что можно успешно добавить две разные книги в коллекцию через метод add_new_book. Убеждается, что обе книги присутствуют в словаре books_genre.
2. test_add_new_book_long_name_not_added
Проверяет ограничение на длину названия: книга с именем из 41 символа не добавляется в коллекцию.
3. test_add_new_book_empty_name_not_added
Проверяет, что книга с пустым названием ('') не добавляется — соблюдается валидация входных данных.
4. test_add_new_book_duplicate_not_added
Убеждается, что повторное добавление уже существующей книги игнорируется, и количество книг в коллекции не увеличивается.
5. test_add_new_book_no_genre_by_default
Проверяет, что у новой добавленной книги изначально нет жанра — значение в словаре books_genre равно пустой строке ''.
6. test_set_and_get_book_genre_correct (параметризованный)
Проверяет корректную установку и получение жанра для разных книг и жанров («Детективы», «Фантастика», «Мультфильмы») с помощью методов set_book_genre и get_book_genre.
7. test_set_book_genre_invalid_genre_not_set
Убеждается, что при попытке установить несуществующий жанр (например, «Неизвестный жанр») жанр книги не изменяется и остаётся пустым.
8. test_set_book_genre_nonexistent_book_not_set
Проверяет, что установка жанра для несуществующей книги не приводит к ошибке и не создаёт новую запись в books_genre.
9. test_get_books_with_specific_genre_returns_correct_list
Проверяет, что метод get_books_with_specific_genre корректно возвращает список книг заданного жанра (в тесте — две книги в жанре «Фантастика»).
10. test_get_books_with_specific_genre_empty_for_invalid_genre
Убеждается, что запрос книг по несуществующему жанру возвращает пустой список, а не вызывает ошибку.
11. test_get_books_for_children_excludes_age_rating_genres
Проверяет, что метод get_books_for_children не включает книги с жанрами из списка возрастного рейтинга ('Ужасы', 'Детективы').
12. test_get_books_for_children_excludes_books_without_genre
Убеждается, что книги без установленного жанра (с пустым значением '') не включаются в список для детей, так как их жанр не входит в возрастной рейтинг.
13. test_add_book_in_favorites_success
Проверяет успешное добавление существующей книги в избранное через метод add_book_in_favorites.
14. test_add_book_in_favorites_not_added_if_not_in_books_genre
Убеждается, что книга, отсутствующая в books_genre, не может быть добавлена в избранное.
15. test_add_book_in_favorites_duplicate_not_added
Проверяет, что повторное добавление одной и той же книги в избранное игнорируется — дубликаты запрещены.
16. test_delete_book_from_favorites_success
Проверяет корректное удаление книги из избранного с помощью метода delete_book_from_favorites.
17. test_delete_book_from_favorites_not_in_favorites_no_error
Убеждается, что попытка удалить книгу, не находящуюся в избранном, не вызывает ошибку и не нарушает состояние системы.
18. test_get_list_of_favorites_books_returns_correct_list
Проверяет, что метод get_list_of_favorites_books возвращает актуальный и полный список избранных книг.