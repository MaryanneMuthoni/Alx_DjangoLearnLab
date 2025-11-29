# Update the title of “1984” to “Nineteen Eighty-Four” 

```python
# Retrieve the book instance first
book = Book.objects.get(title="1984")

# change the title attribute
book.title = "Nineteen Eighty-Four"

# save changes
book.save()

# check change
book.title

# Expected output:
# 'Nineteen Eighty-Four'
