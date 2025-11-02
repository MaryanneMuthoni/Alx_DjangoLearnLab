# Retrieve and display all attributes of the book you just created

```python
# Retrieve the book instance first (assuming it's the only book)
book = Book.objects.get(title="1984")

# Display the attributes
book.title
# Expected output: '1984'

book.author
# Expected output: 'George Orwell'

book.publication_year
# Expected output: '1949'
