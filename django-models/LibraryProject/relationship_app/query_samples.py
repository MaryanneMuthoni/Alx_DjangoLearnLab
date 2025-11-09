# Prepare a Python script query_samples.py in the relationship_app directory. 
# This script should contain the query for various relationship

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    """Query all books by a specific author."""
    # Filter books where the related author's name matches the given name
    books = Book.objects.select_related('author').filter(author__name=author_name)
    return books

# List all books in a library
def list_books_in_library(library_name):
    """List all books in a library"""
    library = Library.objects.get(name=library_name)
    books = library.books.all()


# Retrieve the librarian for a library
def librarian_library(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)
    librarian = library.Librarian
    return librarian


