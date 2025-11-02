# Update the title of “1984” to “Nineteen Eighty-Four” 

```python
# Retrieve the book instance first
book1 = Book.objects.get(title="1984")

# change the title attribute
book1.title = "Nineteen Eighty-Four"

# save changes
book1.save()

# check change
book1.title

# Expected output:
# 'Nineteen Eighty-Four'
