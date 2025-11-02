# Create Book Instance

```python
from bookshelf.models import Book

# create object
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book1
# Expected output: <Book: Book object (None)>
