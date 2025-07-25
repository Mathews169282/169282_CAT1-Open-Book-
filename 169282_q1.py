class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"'{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"You did not borrow '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"\n{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No borrowed books.")

# Sample interaction
if __name__ == "__main__":
    b1 = Book("The Alchemist", "Paulo Coelho")
    b2 = Book("Sapiens", "Yuval Noah Harari")
    member = LibraryMember("Alice", "LM001")

    while True:
        print("\nLibrary Menu")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. List Borrowed Books")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            title = input("Enter book title (The Alchemist / Sapiens): ").strip()
            if title.lower() == "the alchemist":
                member.borrow_book(b1)
            elif title.lower() == "sapiens":
                member.borrow_book(b2)
            else:
                print("Book not found.")

        elif choice == "2":
            title = input("Enter book title to return: ").strip()
            if title.lower() == "the alchemist":
                member.return_book(b1)
            elif title.lower() == "sapiens":
                member.return_book(b2)
            else:
                print("Book not recognized.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
