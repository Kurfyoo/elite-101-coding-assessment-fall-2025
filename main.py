from library_books import library_books
from datetime import datetime, timedelta
import toolbox as tb

def print_book(book, clr=True):
    print(f"id: {book["id"]}")
    print(f"title: {book["title"]}")
    print(f"author: {book["author"]}")
    print(f"genre: {book["genre"]}")
    print(f"available: {book["available"]}")
    print(f"due date: {book["due_date"]}")
    print(f"checkouts: {book["checkouts"]}")
    print("--------------------------------------------")
    if clr:
        tb.wait()

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def view():
    include = input("Include unavailable books? (y/n) ")
    
    print()
    print("available books")
    print("--------------------------------------------")
    
    none = True
    for book in library_books:
        if book["available"] or include == "y":
            print_book(book)
            none = False
    print("END BOOKS")
    if none:
        print("no books found.")
        print("--------------------------------------------")

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search():
    search_type = input("Are you searching by author or genre? ").lower()
    
    if search_type == "author":
        author = input("ENTER AUTHOR: ").title()
        
        print()
        print("matching books")
        print("--------------------------------------------")
        
        none = True
        for book in library_books:
            if book["author"] == author:
                print_book(book)
                none = False
        print("END BOOKS")
        if none:
            print("no books found.")
            print("--------------------------------------------")
    
    elif search_type == "genre":
        genre = input("ENTER GENRE: ").title()
        
        print()
        print("matching books")
        print("--------------------------------------------")
        
        none = True
        for book in library_books:
            if book["genre"] == genre:
                print_book(book)
                none = False
        print("END BOOKS")
        if none:
            print("no books found.")
            print("--------------------------------------------")
    
    else:
        print("INVALID SEARCH TYPE")

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout():
    identity = input("ENTER BOOK ID: ").upper()
    
    none = True
    print()
    print("--------------------------------------------")
    for i, book in enumerate(library_books):
        if book["id"] == identity:
            print_book(book, False)
            idx = i
            none = False
    if none or not library_books[idx]["available"]:
        print("no books found.")
        print("--------------------------------------------")
        return
    
    correct = input("Is this your book? (y/n) ")
    if correct != "y":
        return
    
    if library_books[idx]["available"]:
        library_books[idx]["available"] = False
        library_books[idx]["due_date"] = (datetime.now() + timedelta(weeks=2) ).strftime("%Y-%m-%d")
        library_books[idx]["checkouts"] += 1

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book():
    pass

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def list_overdue():
    pass

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

def menu():
    pass

if __name__ == "__main__":
    tb.clear()
    view()
    tb.wait()
    checkout()
    tb.wait()
    view()
    pass
