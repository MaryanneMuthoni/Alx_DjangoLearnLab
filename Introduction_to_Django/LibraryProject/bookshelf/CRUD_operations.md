<!-- Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949 -->
book1 = Book(title='1984', author='George Orwell', publication_year=1949)
book1.save()
<!-- <Book: Book object (1)>  -->

<!-- Retrieve and display all attributes of the book you just created. -->
book1.title
<!-- '1984' -->
book1.author
<!-- 'George Orwell' -->
book1.publication_year
<!-- 1949 -->

<!-- Update the title of “1984” to “Nineteen Eighty-Four” and save the changes. -->
book1.title = 'Nineteen Eighty-Four'
book1.save()
book1.title
<!-- 'Nineteen Eighty-Four' -->

<!-- Delete the book you created and confirm the deletion by trying to retrieve all books again -->
book1.delete()
<!-- (1, {'bookshelf.Book': 1}) -->
Book.objects.all()
<!-- <QuerySet []> -->
