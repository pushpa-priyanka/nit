from utils import databases

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'f' to find a book
- 'u' to update a book
- 'q' to quit

Your choice: """

def menu():
    databases.create_book_list()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            prompt_list_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        elif user_input == 'f':
            prompt_find_book()
        elif user_input == 'u':
            prompt_update_book()
            
        user_input = input(USER_CHOICE)
            
            
            
def prompt_add_book():
    name = input("Enter name of the book:")
    author = input("Enter name of the author:")
    
    databases.insert_book(name,author)
    
def prompt_list_book():
    for book in databases.get_all_books():
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']} — Read: {read}")

def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    
    databases.mark_book_read(name)

def prompt_find_book():
    name = input('Enter the name of the book you want: ')
    
    databases.find_book(name)
    
def prompt_update_book():
    name = input('Enter the name of the book you want to update: ')
    new_name = input('Enter the new name for the book: ')
    author_change = input('Want you change author also? Enter (y/n) y - yes: n - no;')
    
    databases.update_book(name, new_name, author_change)

def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    
    databases.delete_books(name)    

menu()
    
