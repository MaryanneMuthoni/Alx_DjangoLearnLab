# Retrieve and display all attributes of the book you just created

```python
# Retrieve the book instance first (assuming it's the only book)
book1 = Book.objects.get(title="1984")

# Display the attributes
book1.title
# Expected output: '1984'

book1.author
# Expected output: 'George Orwell'

book1.publication_year
# Expected output: '1949'
