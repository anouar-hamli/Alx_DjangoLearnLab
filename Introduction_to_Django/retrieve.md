



```markdown
```python
from bookshelf.models import Book

# Retrieve the created book
book = Book.objects.get(title="1984")

# Display all attributes
print(book.title, book.author, book.publication_year)
