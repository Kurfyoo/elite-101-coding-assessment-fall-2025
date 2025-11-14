from library_books import library_books, Book
from datetime import datetime, timedelta
import toolbox as tb
import json

# modulation functions

""" -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author """

def view():
    include = input("INCLUDE UNAVAILABLE BOOKS? (y/n) ")
    while include not in ["y", "n"]:
        print("invalid input.")
        include = input("INCLUDE UNAVAILABLE BOOKS? (y/n) ")
    
    print("\navailable books")
    print("--------------------------------------------")
    if library_books:
        for book in library_books:
            if include == "y" or book.available:
                book.print_info()
        print("end books.")
    else:
        print("no books found.")
        print("--------------------------------------------")
    tb.wait()

""" -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books """

def search():
    search_type = input("ARE YOU SEARCHING BY AUTHOR, TITLE, OR GENRE? ").lower()
    while search_type not in ["author", "title", "genre"]:
        print("invalid input.")
        search_type = input("ARE YOU SEARCHING BY AUTHOR, TITLE, OR GENRE? ").lower()

    if search_type == "author":
        author = input("ENTER AUTHOR: ").lower()
        
        print("\nmatching books")
        print("--------------------------------------------")
        if library_books:
            for book in library_books:
                if author in book.author.lower():
                    book.print_info()
            print("end books.")
        else:
            print("no books found.")
            print("--------------------------------------------")
    
    elif search_type == "title":
        title = input("ENTER TITLE: ").lower()
        
        print("\nmatching books")
        print("--------------------------------------------")
        if library_books:
            for book in library_books:
                if title in book.title.lower():
                    book.print_info()
            print("end books.")
        else:
            print("no books found.")
            print("--------------------------------------------")
    
    elif search_type == "genre":
        genre = input("ENTER GENRE: ").title()
        
        print("\nmatching books")
        print("--------------------------------------------")
        if library_books:
            for book in library_books:
                if book.genre == genre:
                    book.print_info()
            print("end books.")
        else:
            print("no books found.")
            print("--------------------------------------------")
    
    tb.wait()

""" -------- Level 3 --------
    # TODO: Create a function to checkout a book by ID
    # If the book is available:
    #   - Mark it unavailable
    #   - Set the due_date to 2 weeks from today
    #   - Increment the checkouts counter
    # If it is not available:
    #   - Print a message saying it's already checked out """

def checkout():
    to_checkout = input("ENTER ID OF BOOK TO BE CHECKED OUT: ").upper()
    while to_checkout not in [book.id for book in library_books]:
        print("invalid book ID.")
        to_checkout = input("ENTER ID OF BOOK TO BE CHECKED OUT: ").upper()

    print("\n--------------------------------------------")
    
    for i, obj in enumerate(library_books):
        if obj.id == to_checkout:
            obj.print_info()
            book_idx = i
            break

    correct = input(f"\nIS THIS BOOK RIGHT? (y/n) ")
    if correct == "y":
        if library_books[book_idx].available:
            print(f"\nchecking out book {book_idx + 1}...")
            library_books[book_idx].available = False
            library_books[book_idx].due_date = (datetime.now() + timedelta(weeks=2) ).strftime("%Y-%m-%d")
            library_books[book_idx].checkouts += 1
        else:
            print(f"\nbook {book_idx + 1} already checked out.")
    
    tb.wait()

""" -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date """

def return_book():
    to_return = input("ENTER ID OF BOOK TO BE RETURNED: ").upper()
    while to_return not in [book.id for book in library_books]:
        print("invalid book ID.")
        to_return = input("ENTER ID OF BOOK TO BE RETURNED: ").upper()

    print("\n--------------------------------------------")

    for i, obj in enumerate(library_books):
        if obj.id == to_return:
            obj.print_info()
            book_idx = i
            break

    correct = input(f"\nIS THIS BOOK RIGHT? (y/n) ")
    if correct == "y":
        if library_books[book_idx].available:
            print(f"\nbook {book_idx + 1} already returned.")
        else:
            print(f"\nreturning book {book_idx + 1}...")
            library_books[book_idx].available = True
            library_books[book_idx].due_date = None
    
    tb.wait()

"""
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
"""

def list_overdue():
    print("\noverdue books")
    print("--------------------------------------------")
    if library_books:
        for book in library_books:
            if not book.due_date is None and book.due_date < datetime.now().strftime("%Y-%m-%d"):
                book.print_info()
        print("end books.")
    else:
        print("no books found.")
        print("--------------------------------------------")

""" -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc. """

def export_libary():
    # Convert Book objects to dictionaries for JSON serialization
    books_data = []
    for book in library_books:
        books_data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "available": book.available,
            "due_date": book.due_date,
            "checkouts": book.checkouts
        })
    
    # Generate JSON string
    json_string = json.dumps(books_data, indent=4)
    
    print("\nlibrary export data:")
    print("--------------------------------------------")
    print(json_string)
    print("--------------------------------------------")
    print("\nCopy the JSON above, make a file named library.json, and paste this string in it.")
    tb.wait()

def import_libary():
    global library_books
    # Load the data back from the JSON file
    try:
        with open("library.json", "r") as file:
            books_data = json.load(file)
        
        # Convert dictionaries back to Book objects
        library_books.clear()
        for book_dict in books_data:
            book = Book(
                book_dict["id"],
                book_dict["title"],
                book_dict["author"],
                book_dict["genre"],
                book_dict["available"],
                book_dict["due_date"],
                book_dict["checkouts"]
            )
            library_books.append(book)
        
        print("library imported successfully from library.json")
    except FileNotFoundError:
        print("library.json file not found, you need to upload it first.")
    tb.wait()

""" -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system! """

def menu():
    print("library menu")
    print("--------------------------------------------")
    print("0) view books")
    print("1) search books")
    print("2) checkout book")
    print("3) return book")
    print("4) list overdue books")
    print("5) export library")
    print("6) import library")
    print("--------------------------------------------")
    while True:
        try:
            choice = int(input("\nENTER A NUMBER (0-6): "))
            if choice in range(7):
                break
        except ValueError:
            pass
        print("please enter a number between 0 and 4.")
    tb.clear()
    if choice == 0:
        view()
    elif choice == 1:
        search()
    elif choice == 2:
        checkout()
    elif choice == 3:
        return_book()
    elif choice == 4:
        list_overdue()
    elif choice == 5:
        export_libary()
    else:
        import_libary()

def main():
    while True:
        tb.clear()
        menu()

if __name__ == "__main__":
    main()
