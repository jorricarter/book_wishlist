import datetime

CURRENT_DATE = datetime.datetime.now()

book_list = []
counter = 0

def search_books(book_title):
    ''' Takes title as argument. Returns books with matching titles. '''

    global book_list
    # This loops through all books, checks if title matches search, adds matches to 'found_books'
    found_books = [book for book in book_list if book.title == book_title]
    return found_books


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [book for book in book_list if book.read == kwargs['read']]
        return read_books


def edit_book(book_id, new_info):
    '''Update book with given book_id to new title and/or author.'''
    global book_list

    for book in book_list:

        if book.id == book_id:
            book.title = new_info.title
            book.author = new_info.author
            return True


def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id()
    book_list.append(book)


def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            book.date = '%d/%d/%d' % (CURRENT_DATE.month, CURRENT_DATE.day, CURRENT_DATE.year)
            book.rating = int(input('Enter a rating for this book 1-10: '))
            return True

    return False  # return False if book id is not found


def check_read(new_book):
    '''Check if a book with the same author and title already exists'''
    global book_list

    for book in book_list:
        if book.title == new_book.title:
            if book.author == new_book.author:
                return True
    return False


def delete_book(book_id):
    '''deleting book from wishlist. Return true is book is found in DB and update is made'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book_list.remove(book)
            return True





