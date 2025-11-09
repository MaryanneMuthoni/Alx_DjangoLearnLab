from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian

# Create your views here.

def book_list(request):
    '''Lists all books stored in the database
    view should render a simple text list of book titles and their authors'''
    books = Book.objects.select_related('author').all()
    context = {'books': books}
    return render(request, 'books/list_books.html', context)

class LibraryDetailView(DetailView):
    '''displays details for a specific library, listing all books available in that library'''
    model = Library
    template_name = 'libraries/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add all books available in this library to the context."""
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
