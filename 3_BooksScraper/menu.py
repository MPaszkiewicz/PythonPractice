from main import books


USER_CHOICE = '''Choose your option:
- 'b' to view all 5-star books
- 'c' to view cheapest books
- 'n' to view next books from catalogue
- 'q' to quit
Enter your choice:'''


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating, reverse=True)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


def print_best_and_cheapest_books():
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)


books_gen = (print(b) for b in books)


def print_next_book():
    global books_gen
    try:
        next(books_gen)
    except StopIteration:
        print('Reached the end of books catalogue, starting from top.')
        books_gen = (print(b) for b in books)
        print_next_book()


menu_functions_map = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book
}

user_input = input(USER_CHOICE)
while user_input != 'q':
    func = menu_functions_map.get(user_input, lambda: print('Invalid option.'))
    func()
    user_input = input(USER_CHOICE)
