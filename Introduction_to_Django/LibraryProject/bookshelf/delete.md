# Delete the book you created and confirm the deletion by trying to retrieve all books again

```python
# Retrieve the book instance first
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

Book.objects.all()
# Expected Output:
# <QuerySet []>
