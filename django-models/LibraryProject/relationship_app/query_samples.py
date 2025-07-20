import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Example: Query all books by a specific author
    author_name = "John Doe"
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # Example: List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    # Example: Retrieve the librarian for a library
    librarian = library.librarian  # Uses related_name
    print(f"Librarian for {library_name}: {librarian.name}")

if __name__ == "__main__":
    run_queries()
