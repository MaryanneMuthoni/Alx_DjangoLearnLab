# contain the query for each of the following of relationships

from .models import Author, Book, Library, Librarian
# Query all books by a specific author
book.author.name

# List all books in a library.
library.books.title

# Retrieve the librarian for a library
librarian.library.name
