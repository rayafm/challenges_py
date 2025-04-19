# Library
# Wizards are having a hard time keeping track of all the books in their library. 
# They need your help to create a library system that will allow them to add, remove, and search for books.

# Magical incantations to find books have unfortunately not been invented yet. 

# Challenge
# You've been tasked with writing the code for the wizard library. 
# Complete the Library and Book classes listed below.

# Create the Book Class:
# Create the __init__(self, title, author) method
# Set .title and .author to the values of the parameters.
# Create the Library Class:
# Create the __init__(self, name) method
# Initialize a .name member variable to the value of the name parameter.
# Create a .books member initialized to an empty list.
# Add the add_book(self, book) method:
# Add book, the given Book instance, to the library's books instance variable by appending it to the end of the list.
# Add the remove_book(self, book) method:
# If the book's title and author match a library book's title and author, remove that library book from the list.
# Add the search_books(self, search_string) method:
# For every book in the library check if the search_string is contained in the title or author field (case-insensitive).
# Return a list of all books that match the search string, ordered in the same order as they were added to the library.
# After a book is removed, it should no longer be returned in the search results.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        for lib_bk in self.books:
            if(book.title == lib_bk.title) and (book.author == lib_bk.author):
                self.books.remove(lib_bk)

    def search_books(self, search_string):
        res = []

        for book in self.books:
            if(search_string in book.title.lower()) or (search_string in book.author.lower()):
                res.append(book)

        return res
