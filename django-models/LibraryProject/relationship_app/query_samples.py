from .models import Author, Book, Library, Librarian

# Contain the query for each of the following of relationships:

# Query all books by a specific author
book.author.name

# List all books in a library.
books.library.all()

# Retrieve the librarian for a library
librarian.library.name

if __name__ == "__main__":
    # code to run when the script is executed directly
    main()

