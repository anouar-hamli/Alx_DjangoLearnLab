```python
from bookshelf.models import Book

# Create a new Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Confirm creation
print(book)
