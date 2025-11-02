# Delete the book you created and confirm the deletion by trying to retrieve all books again

```python
# Retrieve the book instance first
book1 = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book1.delete()

Book.objects.all()
# Expected Output:
# <QuerySet []>
