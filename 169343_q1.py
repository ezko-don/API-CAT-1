class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = [] # it is an empty list because it is the starting point.

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is currently borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


def main():
    # Create some books
    book1 = Book("Gifted Hands", "Ben Carson")
    book2 = Book("Can't Hurt Me", "David Gongins")
    book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")
    book4 = Book("Kigogo", "Assumpta K.Matei")

    # Create a library member
    member = LibraryMember("Ezko", 1)
   # member = LibraryMember("Maya", 2)

    # Interactive loop for borrowing and returning books
    while True:
        action = input(" Hello!Would you like to borrow or return a book? (borrow/return/end to quit): ").lower()
        if action == 'borrow':
            book_title = input("Enter the title of the book to borrow: ")
            if book_title == book1.title:
                member.borrow_book(book1)
            elif book_title == book2.title:
                member.borrow_book(book2)
            elif book_title == book3.title:
                member.borrow_book(book3)
            elif book_title == book4.title:
                member.borrow_book(book4)
            else:
                print("Book not found.")

        elif action == 'return':
            book_title = input("Enter the title of the book to return: ")
            if book_title == book1.title:
                member.return_book(book1)
            elif book_title == book2.title:
                member.return_book(book2)
            elif book_title == book3.title:
                member.return_book(book3)
            else:
                print("Book not found.")

        elif action == 'end':
            break

        member.list_borrowed_books()


if __name__ == "__main__":
    main()