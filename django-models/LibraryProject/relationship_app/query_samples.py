from .models import Author, Book, Library, Librarian

# Contain the query for each of the following of relationships:

# Query all books by a specific author
Book.objects.all()
author.all()

# List all books in a library.
Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library
Librarian.objects.get(name=librarian_name)
library.all()

if __name__ == "__main__":
    # code to run when the script is executed directly
    main()

