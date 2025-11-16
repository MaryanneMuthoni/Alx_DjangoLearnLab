# create.md
# Create Book Instance

from bookshelf.models import Book
# create object
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book1
# Expected output: <Book: Book object (None)>


# retrieve.md
# Retrieve and display all attributes of the book you just created

# Retrieve the book instance first (assuming it's the only book)
book1 = Book.objects.get(title="1984")
# Display the attributes
book1.title
# Expected output: '1984'
book1.author
# Expected output: 'George Orwell'
book1.publication_year
# Expected output: '1949'


# update.md
# Update the title of “1984” to “Nineteen Eighty-Four” 

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


#delete.md
# Delete the book you created and confirm the deletion by trying to retrieve all books again

# Retrieve the book instance first
book1 = Book.objects.get(title="Nineteen Eighty-Four")
# Delete the book
book1.delete()
Book.objects.all()
# Expected Output:
# <QuerySet []>
