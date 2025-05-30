# Day 19 - Library Management System using OOP

# define Library class
class Library:
    def __init__(self, book_list):  # constructor to initialize books
        self.available_books = book_list  # list of available books
        self.borrowed_books = {}  # dictionary to track borrowed books

    def display_books(self):  # display all available books
        print("Available books in the library:")
        for book in self.available_books:
            print(f'- {book}')

    def borrow_book(self, book_name, user_name):  # borrow a book
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.borrowed_books[book_name] = user_name
            print(f'{user_name} has borrowed "{book_name}"')
        elif book_name in self.borrowed_books:
            print(f'"{book_name}" is already borrowed by {self.borrowed_books[book_name]}')
        else:
            print('Book not found')

    def return_book(self, book_name, user_name):  # return a borrowed book
        if book_name in self.borrowed_books and self.borrowed_books[book_name] == user_name:
            del self.borrowed_books[book_name]
            self.available_books.append(book_name)
            print(f'{user_name} has returned "{book_name}"')
        else:
            print('Return failed: Either book not borrowed or wrong user')

# sample usage
books = ["Python Crash Course", "Deep Learning", "Clean Code", "AI for Beginners"]
library = Library(books)

library.display_books()
library.borrow_book("Python Crash Course", "Ali")
library.display_books()
library.return_book("Python Crash Course", "Ali")
library.display_books()
