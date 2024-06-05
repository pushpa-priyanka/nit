books = []

def create_book_list():
    pass

def get_all_books():
    return books

def insert_book(name, author):
    books.append({'name':name, 'author':author, 'read':False})
    
def mark_book_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            
    
def find_book(name):
    for book in books:
        if name == book['name']:
            read = 'Yes' if book['read'] else 'No'
            print(f"{book['name']} by {book['author']} — Read: {read}")
        
def update_book(name, new_name, author_change):
    for book in books:
        if book['name'] == name:
            book['name'] = new_name
            if author_change == 'y':
                book['author'] =  input('Enter the name of new author: ')
                
def delete_books(name):
    global books
    books = [book for book in books if book['name'] != name]