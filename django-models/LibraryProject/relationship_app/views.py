from django.shortcuts import render
from .models import Author
from .models import Book
from .models import Library
from .models import Librarian
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    '''Lists all books stored in the database'''
    books = Book.objects.all()
    context= {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    '''Displays details for a specific library, listing all books available in that library'''
    model = Library
    template_name = 'relationship_app/library_detail.html'


