import os
from book import Book

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')


separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0


def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    try:
        with open(BOOKS_FILE_NAME) as f:
            data = f.read()
            make_book_list(data)
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass

    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass  # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        f.write(output_data)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))


def make_book_list(string_from_file):
    ''' turn the string from the file into a list of Book objects'''

    global book_list

    books_str = string_from_file.split('\n')

    for book_str in books_str:
        data = book_str.split(separator)
        book = Book(data[0], data[1], data[2] == 'True', int(data[3]))
        book_list.append(book)

def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    for book in book_list:
        output = [ book.title, book.author, str(book.read), str(book.id) ]
        output_str = separator.join(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string

