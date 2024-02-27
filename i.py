from abc import ABC, abstractmethod

# Define Book class
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

# Define smaller, more specific interfaces

class BookSearch(ABC):
    @abstractmethod
    def search_by_title(self, title):
        pass
    
    @abstractmethod
    def search_by_author(self, author):
        pass
    
    @abstractmethod
    def search_by_genre(self, genre):
        pass

class BookManagement(ABC):
    @abstractmethod
    def add_book(self, book):
        pass
    
    @abstractmethod
    def remove_book(self, book):
        pass

class BookLoan(ABC):
    @abstractmethod
    def borrow_book(self, user, book):
        pass
    
    @abstractmethod
    def return_book(self, user, book):
        pass

class ReportGeneration(ABC):
    @abstractmethod
    def generate_borrowing_report(self):
        pass
    
    @abstractmethod
    def generate_overdue_report(self):
        pass
    
    @abstractmethod
    def generate_popularity_report(self):
        pass

# Implement classes adhering to specific interfaces

class GuestUser(BookSearch):
    def __init__(self, catalog):
        self.catalog = catalog

    def search_by_title(self, title):
        books = self.catalog.search_by_title(title)
        print(f"Books found with title '{title}':")
        for book in books:
            print(f"- {book.title} by {book.author}")

    def search_by_author(self, author):
        books = self.catalog.search_by_author(author)
        print(f"Books found by author '{author}':")
        for book in books:
            print(f"- {book.title} by {book.author}")

    def search_by_genre(self, genre):
        books = self.catalog.search_by_genre(genre)
        print(f"Books found in genre '{genre}':")
        for book in books:
            print(f"- {book.title} by {book.author}")

class Librarian(BookSearch, BookManagement, BookLoan, ReportGeneration):
    def __init__(self, catalog):
        self.catalog = catalog

    def search_by_title(self, title):
        return self.catalog.search_by_title(title)

    def search_by_author(self, author):
        return self.catalog.search_by_author(author)

    def search_by_genre(self, genre):
        return self.catalog.search_by_genre(genre)

    def add_book(self, book):
        self.catalog.add_book(book)
        print(f"Book '{book.title}' added to the catalog.")

    def remove_book(self, book):
        self.catalog.remove_book(book)
        print(f"Book '{book.title}' removed from the catalog.")

    def borrow_book(self, user, book):
        # Assume some borrowing logic here
        print(f"User '{user}' borrowed book '{book.title}'.")

    def return_book(self, user, book):
        # Assume some returning logic here
        print(f"User '{user}' returned book '{book.title}'.")

    def generate_borrowing_report(self):
        # Placeholder implementation for generating borrowing report
        print("Generating borrowing report...")

    def generate_overdue_report(self):
        # Placeholder implementation for generating overdue report
        print("Generating overdue report...")

    def generate_popularity_report(self):
        # Placeholder implementation for generating popularity report
        print("Generating popularity report...")

# Implement Catalog class
class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def search_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def search_by_genre(self, genre):
        return [book for book in self.books if book.genre == genre]

# Example usage
if __name__ == "__main__":
    catalog = Catalog()
    catalog.add_book(Book("Python Programming", "Guido van Rossum", "Programming"))
    catalog.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))

    guest = GuestUser(catalog)
    guest.search_by_title("Python Programming")
    guest.search_by_author("F. Scott Fitzgerald")

    librarian = Librarian(catalog)
    librarian.add_book(Book("Clean Code", "Robert C. Martin", "Programming"))
    librarian.remove_book(catalog.search_by_title("The Great Gatsby")[0])
    librarian.generate_borrowing_report()
