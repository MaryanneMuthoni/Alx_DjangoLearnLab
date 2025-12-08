<!-- Delete the book you created and confirm the deletion by trying to retrieve all books again -->
book1.delete()
<!-- (1, {'bookshelf.Book': 1}) -->
Book.objects.all()
<!-- <QuerySet []> -->
