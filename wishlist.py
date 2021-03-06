# Main program

import ui, datastore, file
from book import Book


def handle_choice(choice):
    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        del_book()

    elif choice == '6':
        edit_book()

    elif choice == '7':
        search_book()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def search_book():
    '''Get title from user. Show books with matching titles.'''
    book_title = ui.ask_for_book_title()
    found_books = datastore.search_books(book_title)
    ui.show_list(found_books)


def edit_book():
    '''Get choice from user, edit a book's Title or Author'''
    book_id = ui.ask_for_book_id()
    new_info = ui.get_new_book_info()
    if datastore.edit_book(book_id, new_info):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    if datastore.check_read(new_book):
        ui.message('THIS BOOK IS A DUPLICATE OF ANOTHER BOOK IN THE SYSTEM!')
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))


def del_book():
    '''deleting book from list based on id'''
    book_id = ui.ask_for_book_id()
    if datastore.delete_book(book_id):
        ui.message('BOOK REMOVED FROM DATABASE')
    else:
        ui.message('Book not found, please try again.')


def quit():
    '''Perform shutdown tasks'''
    file.shutdown()
    ui.message('Bye!')


def main():
    file.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
