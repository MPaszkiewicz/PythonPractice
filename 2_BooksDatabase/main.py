import utils.database as database

USER_CHOICE = """
Enter:
- 'a' to add new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""

test_input = open('testinput.txt', 'r')


def user_input(prompt):
    if not test_input.closed:
        line = test_input.readline().strip()
        if len(line) == 0:
            test_input.close()
        else:
            return line
    return input(prompt)


def add_book():
    name, author = user_input("Provide comma separated book name and author: ").split(',')
    database.add(name.strip(), author.strip(), False)


def list_books():
    for book in database.get_all():
        print("name: {}, author: {}, read: {}".format(book['name'], book['author'], 'Yes' if book['read'] else 'No'))
    print()


def mark_read():
    name = user_input("Provide name of book which you read: ")
    database.update_read(name.strip(), True)


def delete_book():
    name = user_input("Provide name of book for deletion: ")
    database.remove(name.strip())


choice_functions = {
    'a': add_book,
    'l': list_books,
    'r': mark_read,
    'd': delete_book
}


def get_choice():
    return user_input(USER_CHOICE)


def menu():
    choice = get_choice()
    while choice != 'q':
        #print('chose operation {}'.format(choice))
        if choice in choice_functions.keys():
            choice_functions[choice]()
        else:
            print("Please choose valid operation.")
        choice = get_choice()


menu()
