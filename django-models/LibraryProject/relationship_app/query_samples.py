from .models import Author, Book, Library, Librarian

# Contain the query for each of the following of relationships:

# Query all books by a specific author
Author.objects.get(name=author_name)
objects.filter(author=author)

# List all books in a library.
Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library
Library.objects.get(name=library_name)
objects.filter(library=library)

if __name__ == "__main__":
    # code to run when the script is executed directly
    main()

