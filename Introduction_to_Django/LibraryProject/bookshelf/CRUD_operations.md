<!-- Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949 -->
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
book.save()
<!-- <Book: Book object (1)>  -->


<!-- Retrieve and display all attributes of the book you just created. -->
Book.objects.get(title='1984', author='George Orwell', publication_year=1949)
<!-- <Book: Book object (1)> -->


<!-- Update the title of “1984” to “Nineteen Eighty-Four” and save the changes. -->
book.title = 'Nineteen Eighty-Four'
book.save()
book.title
<!-- 'Nineteen Eighty-Four' -->


<!-- Delete the book you created and confirm the deletion by trying to retrieve all books again -->
book.delete()
<!-- (1, {'bookshelf.Book': 1}) -->
Book.objects.all()
<!-- <QuerySet []> -->
